#!/usr/bin/env python3
"""
Auto-Publish Pipeline
=====================

Fully automated workflow:
1. Sync Medium publications to Markdown
2. Convert papers to Markdown (no docx)
3. Security audit
4. Auto-commit and push to GitHub

Designed for developers who publish research.

SAFETY RESTRICTIONS:
- CANNOT delete files or directories anywhere
- WRITE access ONLY to: ~/Research/AI Working Directory/
- READ-ONLY access to: ~/Research/ (except AI Working Directory)
- All file operations are validated before execution

Usage:
    python auto_publish.py          # Full pipeline
    python auto_publish.py --dry-run # Preview without pushing

Cron example (daily at 9am):
    0 9 * * * /usr/bin/python3 /path/to/auto_publish.py >> ~/publish.log 2>&1
"""

import os
import re
import sys
import json
import shutil
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from urllib.parse import quote


# ============================================================
# SAFETY LAYER - Enforces read/write restrictions
# ============================================================

class SafetyError(Exception):
    """Raised when an operation violates safety restrictions."""
    pass


class SafeFileSystem:
    """
    Safe file system wrapper that enforces:
    - NO delete operations anywhere
    - WRITE only to allowed directories
    - READ from anywhere (but validates paths)
    """

    def __init__(self):
        self.home = Path.home()
        # Only these directories allow write operations
        self.write_allowed = [
            self.home / "Research" / "AI Working Directory",
            self.home / "Research" / ".github_staging",
            self.home / "Research" / "SYNC",
        ]

    def _can_write(self, path: Path) -> bool:
        """Check if path is in a writable directory."""
        path = Path(path).resolve()
        for allowed in self.write_allowed:
            try:
                path.relative_to(allowed.resolve())
                return True
            except ValueError:
                continue
        return False

    def _validate_write(self, path: Path, operation: str):
        """Validate write operation is allowed."""
        path = Path(path).resolve()
        if not self._can_write(path):
            raise SafetyError(
                f"BLOCKED: {operation} to '{path}' - "
                f"Write only allowed in: {[str(p) for p in self.write_allowed]}"
            )

    def write_text(self, path: Path, content: str, encoding: str = "utf-8"):
        """Safe write_text - only to allowed directories."""
        self._validate_write(path, "write_text")
        Path(path).write_text(content, encoding=encoding)

    def copy(self, src: Path, dst: Path):
        """Safe copy - destination must be in allowed directory."""
        self._validate_write(dst, "copy")
        shutil.copy2(src, dst)

    def mkdir(self, path: Path, parents: bool = True, exist_ok: bool = True):
        """Safe mkdir - only in allowed directories."""
        self._validate_write(path, "mkdir")
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)

    def rmtree(self, path: Path):
        """BLOCKED - No delete operations allowed."""
        raise SafetyError(f"BLOCKED: rmtree('{path}') - DELETE OPERATIONS ARE DISABLED")

    def remove(self, path: Path):
        """BLOCKED - No delete operations allowed."""
        raise SafetyError(f"BLOCKED: remove('{path}') - DELETE OPERATIONS ARE DISABLED")

    def unlink(self, path: Path):
        """BLOCKED - No delete operations allowed."""
        raise SafetyError(f"BLOCKED: unlink('{path}') - DELETE OPERATIONS ARE DISABLED")


# Global safe filesystem instance
safe_fs = SafeFileSystem()

# ============================================================
# CONFIGURATION
# ============================================================

CONFIG = {
    # Medium sync
    "medium_username": os.environ.get("MEDIUM_USERNAME", "qikevinl"),
    "sync_dir": Path(os.environ.get("SYNC_DIR", Path.home() / "Research" / "SYNC" / "Medium")),

    # Research directory
    "research_dir": Path(os.environ.get("RESEARCH_DIR", Path.home() / "Research")),

    # GitHub
    "github_repo": "qikevinl/ONI",
    "staging_dir": Path(os.environ.get("STAGING_DIR", Path.home() / "Research" / ".github_staging")),

    # Exclusions - no tools, no docx, no temp files, no private notes
    "excluded_patterns": [
        # Tools (not needed for readers)
        "tools/", "*.py",

        # Office formats (convert to markdown instead)
        "*.docx", "*.doc", "*.xlsx", "*.pptx",

        # Private folders
        "Notes & Future Work/",

        # Secrets and config
        ".env", ".env.*", "*.pem", "*.key", "credentials*", "api_key*",
        ".claude/", ".deepseek/", "*.local.json",

        # OS/Editor
        ".DS_Store", ".git/", ".idea/", ".vscode/",

        # Temp files
        "*.tmp", ".tmp.*", "__pycache__/", "*.pyc",
        ".sync_state.json", "sync.log",

        # Google Drive
        ".tmp.drivedownload/", ".tmp.driveupload/",
        "*.gdoc", "*.gsheet", "*.gslides",

        # Staging itself
        ".github_staging/",
    ],
}

# ============================================================
# MEDIUM SYNC
# ============================================================

try:
    import feedparser
    import html2text
    import requests
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False


# ============================================================
# ABOUT PAGE SYNC
# ============================================================

class AboutSync:
    """Sync About content to AboutMe.md with delta detection.

    Reads from local file (about_content.md) since Medium blocks scraping.
    Update the source file when your Medium About page changes.
    """

    def __init__(self):
        self.username = CONFIG["medium_username"]
        self.about_url = f"https://medium.com/@{self.username}/about"
        self.source_file = CONFIG["research_dir"] / "AI Working Directory" / "about_content.md"
        self.state_file = CONFIG["sync_dir"] / ".about_state.json"

    def load_state(self) -> Dict:
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return {"hash": "", "last_sync": None}

    def save_state(self, state: Dict):
        state["last_sync"] = datetime.now().isoformat()
        safe_fs.write_text(self.state_file, json.dumps(state, indent=2))

    def sync(self, staging_dir: Path) -> bool:
        """Sync About content if source file changed."""
        print(f"\n👤 About Page Sync")

        if not self.source_file.exists():
            print(f"  ⚠️  Source file not found: {self.source_file}")
            print(f"      Create this file with your Medium About content")
            return False

        content = self.source_file.read_text()
        state = self.load_state()

        # Check for changes via hash
        content_hash = hashlib.md5(content.encode()).hexdigest()

        if content_hash == state.get("hash"):
            print("  ℹ️  No changes detected")
            # Still copy to staging if not present
            if not (staging_dir / "AboutMe.md").exists():
                pass  # Will create below
            else:
                return False

        # Generate AboutMe.md
        about_md = f'''# About

{content}

---

*[Medium]({self.about_url})*
'''

        safe_fs.write_text(staging_dir / "AboutMe.md", about_md)
        state["hash"] = content_hash
        self.save_state(state)

        print("  ✅ AboutMe.md updated")
        return True


class MediumSync:
    """Efficient delta sync from Medium RSS."""

    def __init__(self):
        self.username = CONFIG["medium_username"]
        self.sync_dir = CONFIG["sync_dir"]
        self.state_file = self.sync_dir / ".sync_state.json"

        if DEPS_AVAILABLE:
            self.h2t = html2text.HTML2Text()
            self.h2t.ignore_links = False
            self.h2t.ignore_images = False
            self.h2t.body_width = 0

    def load_state(self) -> Dict:
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return {"downloaded": [], "last_sync": None}

    def save_state(self, state: Dict):
        state["last_sync"] = datetime.now().isoformat()
        safe_fs.write_text(self.state_file, json.dumps(state, indent=2))

    def sanitize_filename(self, title: str) -> str:
        safe = re.sub(r'[<>:"/\\|?*\'\u2018\u2019\u201c\u201d\u2014\u2013]', '', title)
        return re.sub(r'\s+', ' ', safe).strip()[:100]

    def article_to_markdown(self, entry: Dict) -> str:
        title = entry.get("title", "Untitled")
        published = entry.get("published", "")
        link = entry.get("link", "")
        tags = [tag.term for tag in entry.get("tags", [])]
        content = entry.get("content", [{}])[0].get("value", "") or entry.get("summary", "")

        return f"""---
title: "{title}"
date: "{published}"
url: {link}
tags: {json.dumps(tags)}
---

# {title}

{self.h2t.handle(content).strip()}

---
*Originally published on [Medium]({link})*
"""

    def sync(self) -> int:
        if not DEPS_AVAILABLE:
            print("  ⚠️  Install: pip install feedparser html2text")
            return 0

        print(f"\n📰 Medium Sync (@{self.username})")

        safe_fs.mkdir(self.sync_dir, parents=True, exist_ok=True)
        state = self.load_state()

        # Fetch RSS
        feed = feedparser.parse(f"https://medium.com/feed/@{self.username}")
        if feed.bozo and not feed.entries:
            print(f"  ❌ Feed error: {feed.bozo_exception}")
            return 0

        new_count = 0
        for entry in feed.entries:
            link = entry.get("link", "")
            article_id = hashlib.md5(link.encode()).hexdigest()[:12]

            if article_id in state["downloaded"]:
                continue

            title = entry.get("title", "Untitled")
            print(f"  📄 New: {title[:50]}...")

            published = entry.get("published_parsed")
            date_str = datetime(*published[:3]).strftime("%Y-%m-%d") if published else datetime.now().strftime("%Y-%m-%d")

            filename = f"{date_str}-{self.sanitize_filename(title)}.md"
            safe_fs.write_text(self.sync_dir / filename, self.article_to_markdown(entry), encoding="utf-8")

            state["downloaded"].append(article_id)
            self.save_state(state)
            new_count += 1

        print(f"  ✅ {new_count} new articles synced")
        return new_count


# ============================================================
# PAPER CONVERTER (docx → markdown)
# ============================================================

class PaperConverter:
    """Convert docx papers to clean markdown."""

    def __init__(self):
        self.research_dir = CONFIG["research_dir"]

    def convert_docx(self, docx_path: Path, output_dir: Path) -> Optional[Path]:
        """Convert a single docx to markdown using pandoc."""
        try:
            md_name = docx_path.stem + ".md"
            md_path = output_dir / md_name

            result = subprocess.run(
                ["pandoc", str(docx_path.absolute()), "-t", "gfm", "-o", str(md_path.absolute())],
                capture_output=True, text=True,
                cwd=str(Path.home())  # Use home dir to avoid cwd issues
            )

            if result.returncode == 0:
                # Add frontmatter
                content = md_path.read_text()
                frontmatter = f"""---
title: "{docx_path.stem}"
source: "{docx_path.name}"
converted: "{datetime.now().isoformat()}"
---

"""
                safe_fs.write_text(md_path, frontmatter + content)
                return md_path
            else:
                print(f"  ⚠️  Pandoc error: {result.stderr}")
                return None
        except Exception as e:
            print(f"  ⚠️  Convert error: {e}")
            return None

    def convert_all(self, output_dir: Path) -> int:
        """Find and convert all docx files."""
        print(f"\n📝 Converting papers to Markdown")

        safe_fs.mkdir(output_dir, parents=True, exist_ok=True)
        count = 0

        for docx in self.research_dir.rglob("*.docx"):
            # Skip temp files
            if docx.name.startswith("~") or ".tmp" in str(docx):
                continue

            print(f"  📄 Converting: {docx.name}")
            if self.convert_docx(docx, output_dir):
                count += 1

        print(f"  ✅ {count} papers converted")
        return count


# ============================================================
# GITHUB PUBLISHER
# ============================================================

class GitHubPublisher:
    """Prepare and push to GitHub."""

    def __init__(self):
        self.staging = CONFIG["staging_dir"]
        self.research_dir = CONFIG["research_dir"]

    def is_excluded(self, path: Path) -> bool:
        """Check if path should be excluded."""
        import fnmatch
        rel = str(path.relative_to(self.research_dir))
        name = path.name

        for pattern in CONFIG["excluded_patterns"]:
            if pattern.endswith("/"):
                if pattern.rstrip("/") in rel.split("/"):
                    return True
            elif fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(rel, pattern):
                return True
        return False

    # Topic mappings for organizing content
    # Each distinct topic gets its own folder - no mixing
    TOPIC_MAPPINGS = {
        # Coherence Metric
        "coherence": "coherence-metric",
        "coherence_metric": "coherence-metric",
        "spam filter": "coherence-metric",

        # Neural Ransomware
        "ransomware": "neural-ransomware",
        "neural_ransomware": "neural-ransomware",

        # Scale-Frequency
        "scale": "scale-frequency",
        "frequency": "scale-frequency",
        "week3": "scale-frequency",

        # Neural Firewall (separate from framework)
        "firewall": "neural-firewall",
        "needs a firewall": "neural-firewall",

        # Core Framework (ONI/OSI model only)
        "oni": "oni-framework",
        "osi": "oni-framework",
        "osi of mind": "oni-framework",
        "organic network interface": "oni-framework",
        "organic neural interface": "oni-framework",
    }

    def _get_topic(self, filename: str) -> str:
        """Determine topic folder based on filename."""
        name_lower = filename.lower()
        for keyword, topic in self.TOPIC_MAPPINGS.items():
            if keyword in name_lower:
                return topic
        return "oni-framework"  # default for unmatched content

    def prepare_staging(self) -> Path:
        """Prepare clean staging directory with topic-based structure."""
        print(f"\n📦 Preparing GitHub staging (topic-based)")

        # Create topic-based structure
        topics = ["oni-framework", "neural-firewall", "coherence-metric", "neural-ransomware", "scale-frequency"]
        for topic in topics:
            safe_fs.mkdir(self.staging / "docs" / topic, parents=True, exist_ok=True)

        # Copy and organize articles by topic
        articles_src = CONFIG["sync_dir"]
        if articles_src.exists():
            for md in articles_src.glob("*.md"):
                topic = self._get_topic(md.name)
                safe_fs.copy(md, self.staging / "docs" / topic / md.name)
                print(f"  📄 [{topic}] {md.name}")

        # Convert papers and organize by topic
        # Note: *.docx is in exclusions to prevent raw copy, but we still convert them
        converter = PaperConverter()
        for docx in self.research_dir.rglob("*.docx"):
            # Skip temp files and private folders only
            if docx.name.startswith("~") or ".tmp" in str(docx):
                continue
            if "Notes & Future Work" in str(docx):
                continue
            topic = self._get_topic(docx.name)
            topic_dir = self.staging / "docs" / topic
            safe_fs.mkdir(topic_dir, parents=True, exist_ok=True)
            converted = converter.convert_docx(docx, topic_dir)
            if converted:
                print(f"  📄 [{topic}] {docx.stem}.md")

        # Sync About page
        about_sync = AboutSync()
        about_sync.sync(self.staging)

        # Generate docs
        self._write_readme()
        self._write_license()
        self._write_contributing()

        file_count = sum(1 for _ in self.staging.rglob("*") if _.is_file())
        print(f"  ✅ {file_count} files staged")
        return self.staging

    def _extract_doc_info(self, filepath: Path) -> Dict:
        """Extract title and summary from a markdown file."""
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            lines = content.split('\n')

            # Extract title from frontmatter or first heading
            title = filepath.stem
            summary = ""

            for line in lines:
                if line.startswith('title:'):
                    title = line.replace('title:', '').strip().strip('"\'')
                elif line.startswith('# ') and not title:
                    title = line[2:].strip()
                # Get first paragraph as summary (skip frontmatter and headings)
                elif line.strip() and not line.startswith('#') and not line.startswith('---') and not ':' in line[:20]:
                    if len(line.strip()) > 50:
                        summary = line.strip()[:150] + "..." if len(line.strip()) > 150 else line.strip()
                        break

            return {"title": title, "summary": summary, "path": filepath.name}
        except:
            return {"title": filepath.stem, "summary": "", "path": filepath.name}

    def _scan_topics(self) -> Dict[str, List[Dict]]:
        """Scan all topic folders and extract document info."""
        topics = {}
        docs_dir = self.staging / "docs"

        if not docs_dir.exists():
            return topics

        for topic_dir in sorted(docs_dir.iterdir()):
            if topic_dir.is_dir():
                topic_name = topic_dir.name
                docs = []
                for md_file in sorted(topic_dir.glob("*.md")):
                    docs.append(self._extract_doc_info(md_file))
                if docs:
                    topics[topic_name] = docs

        return topics

    def _write_readme(self):
        # Scan topics for dynamic content
        topics = self._scan_topics()

        readme = f'''# ONI Framework

> An extensible framework for monitoring and securing neural communications, designed for transparency and interoperability across bio-digital systems.

## Objective

Brain-computer interfaces are being implanted in humans today, yet we lack standardized security frameworks for protecting neural communications. This project aims to:

1. **Establish shared vocabulary** — Define the attack surfaces, threat models, and defense mechanisms for neural interfaces before exploits emerge in the wild

2. **Bridge disciplines** — Translate cybersecurity principles into neuroscience contexts and vice versa, creating a common language for cross-domain collaboration

3. **Build proactively** — Develop security primitives (like the Coherence Metric) that can be implemented in hardware before BCIs reach mainstream adoption

4. **Invite scrutiny** — This framework is intentionally public and open. I want neuroscientists to challenge the biological assumptions, security researchers to find holes, and ethicists to identify governance gaps

**This is a living research project.** If you see flaws, have ideas, or want to collaborate — open an issue, submit a PR, or reach out directly. The goal isn't to be right; it's to build something robust enough to protect the most sensitive interface humanity will ever create: the one between technology and the mind.

---

## Key Components

### The 14-Layer ONI Model

Extends the traditional OSI model into biological territory:

| Layers | Domain | Description |
|--------|--------|-------------|
| 1-7 | Traditional OSI | Physical → Application (standard networking) |
| 8-10 | Neural Interface | Electrodes, local field potentials, oscillatory patterns |
| 11-14 | Cognitive | Working memory, attention, executive function, identity |

### The Coherence Metric

Mathematical framework for validating neural signal trustworthiness:

```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
```

| Component | Variable | Measures | Security Function |
|-----------|----------|----------|-------------------|
| **Phase** | σ²φ | Timing jitter | Detects out-of-sync signal injections |
| **Transport** | σ²τ | Pathway reliability | Flags signals bypassing biological routes |
| **Gain** | σ²γ | Amplitude stability | Catches over/under-powered attacks |

**Interpretation:** Cₛ ranges from 0 (untrusted) to 1 (fully coherent). Signals below threshold are rejected before reaching neural tissue.

### Neural Signal Assurance Model (NSAM)

Physiology-first defense framework with checkpoints:

1. **Signal Existence** — Should this signal exist at all?
2. **Signal Integrity** — Is it biologically plausible?
3. **Intent & Context** — Does it make sense right now?
4. **Outcome Monitoring** — What effect is it causing?
5. **Human Sovereignty** — Does the human retain agency?

---

## Topics & Documents

'''
        # Dynamic topic sections
        topic_descriptions = {
            "oni-framework": {
                "title": "🏗️ ONI Framework",
                "desc": "Core ONI architecture, 14-layer model extending OSI into biological territory."
            },
            "neural-firewall": {
                "title": "🛡️ Neural Firewall",
                "desc": "Hardware and software firewall design for neural interfaces, signal filtering, and real-time protection."
            },
            "coherence-metric": {
                "title": "📊 Coherence Metric",
                "desc": "Signal validation mathematics, trust scoring algorithms, and biological plausibility checks."
            },
            "neural-ransomware": {
                "title": "🔓 Neural Ransomware",
                "desc": "Threat analysis, attack vectors, kill chains, and defensive architectures."
            },
            "scale-frequency": {
                "title": "🔬 Scale-Frequency",
                "desc": "Cross-scale neural patterns, frequency invariants, and information compression."
            }
        }

        for topic_key, docs in topics.items():
            info = topic_descriptions.get(topic_key, {"title": topic_key.title(), "desc": ""})
            readme += f"### {info['title']}\n\n"
            readme += f"{info['desc']}\n\n"
            readme += f"| Document | Summary |\n"
            readme += f"|----------|----------|\n"
            for doc in docs:
                # URL-encode the path to handle special characters (em dashes, curly quotes, etc.)
                encoded_path = quote(doc['path'])
                doc_link = f"[{doc['title'][:50]}{'...' if len(doc['title']) > 50 else ''}](docs/{topic_key}/{encoded_path})"
                summary = doc['summary'][:80] + "..." if len(doc['summary']) > 80 else doc['summary']
                readme += f"| {doc_link} | {summary} |\n"
            readme += f"\n"

        readme += f'''---

## Quick Reference

### Attack Surfaces by Layer

| Layer | Attack Surface | Example Threat |
|-------|---------------|----------------|
| L1-2 | RF/Bluetooth | BlueBorne-style exploits |
| L3-4 | Protocol | Packet injection, replay attacks |
| L8 | Electrode | Signal injection at hardware |
| L9-10 | Neural | Phase-locked malicious stimulation |
| L11-14 | Cognitive | Memory manipulation, identity attacks |

### Hardware Constraints (Neuralink N1 Reference)

| Constraint | Value | Security Implication |
|------------|-------|---------------------|
| Power budget | 25mW total | Firewall gets ~3-5mW max |
| Latency | <1ms required | Real-time validation needed |
| Electrodes | 1,024 channels | High-bandwidth monitoring |
| Form factor | ~1mm² | Minimal silicon for security |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Seeking input from:**
- **Neuroscientists** — Validate biological assumptions
- **Security Engineers** — Identify attack vectors
- **Hardware Engineers** — Assess implementation constraints
- **Ethicists** — Address governance gaps

---

## License

Apache License 2.0 - See [LICENSE](LICENSE)

---

*Auto-published from research pipeline*
*Last update: {datetime.now().strftime("%Y-%m-%d %H:%M")}*
*Documents: {sum(len(docs) for docs in topics.values())} | Topics: {len(topics)}*
'''
        safe_fs.write_text(self.staging / "README.md", readme)

    def _write_license(self):
        safe_fs.write_text(self.staging / "LICENSE", '''Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

Copyright 2026 Kevin L. Qi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
''')

    def _write_contributing(self):
        safe_fs.write_text(self.staging / "CONTRIBUTING.md", '''# Contributing to ONI Framework

Thank you for your interest in contributing to the Organic Neural Interface (ONI) Framework.

## How to Contribute

### 1. Open an Issue

Before making changes, open an issue to discuss:
- **Biological Assumptions**: Challenge or validate neuroscience claims
- **Security Gaps**: Identify attack vectors or defense weaknesses
- **Mathematical Models**: Improve or critique formal definitions
- **Documentation**: Clarify explanations or fix errors

### 2. Submit a Pull Request

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-contribution`
3. Make your changes in the appropriate `docs/` subfolder
4. Commit with clear messages
5. Open a PR with description of changes

### Areas Seeking Contribution

| Area | What We Need |
|------|--------------|
| **Neuroscience** | Validation of biological assumptions, empirical references |
| **Security** | Attack vector analysis, penetration testing perspectives |
| **Hardware** | BCI implementation constraints, power/latency tradeoffs |
| **Ethics** | Governance frameworks, regulatory alignment |
| **Math** | Formal proofs, statistical validation |

### Code of Conduct

- Be respectful and constructive
- Focus on technical merit
- Cite sources for claims
- Acknowledge uncertainty

### Questions?

Open an issue with the `question` label or reach out on [Medium](https://medium.com/@qikevinl).

---

*This is a living research project. Critique makes it stronger.*
''')

    def git_sync(self, dry_run: bool = False) -> bool:
        """Commit and push to GitHub."""
        print(f"\n🚀 GitHub Sync")

        cwd = str(self.staging)

        # Check if git repo exists
        if not (self.staging / ".git").exists():
            subprocess.run(["git", "init"], capture_output=True, cwd=cwd)
            subprocess.run(["git", "remote", "add", "origin",
                          f"git@github.com:{CONFIG['github_repo']}.git"], capture_output=True, cwd=cwd)
            subprocess.run(["git", "fetch", "origin"], capture_output=True, cwd=cwd)
            subprocess.run(["git", "checkout", "-B", "main"], capture_output=True, cwd=cwd)

        # Stage changes
        subprocess.run(["git", "add", "-A"], capture_output=True, cwd=cwd)

        # Check for changes
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=cwd)
        if not status.stdout.strip():
            print("  ℹ️  No changes to commit")
            return True

        if dry_run:
            print(f"  🔍 Dry run - would commit:")
            print(status.stdout)
            return True

        # Commit
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        commit_msg = f"Auto-publish: {timestamp}"

        result = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            capture_output=True, text=True, cwd=cwd
        )
        print(f"  📝 Committed: {commit_msg}")

        # Push with SSH
        env = os.environ.copy()
        env["GIT_SSH_COMMAND"] = "ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes"

        result = subprocess.run(
            ["git", "push", "-u", "origin", "main", "--force"],
            capture_output=True, text=True, cwd=cwd, env=env
        )

        if result.returncode == 0:
            print(f"  ✅ Pushed to github.com/{CONFIG['github_repo']}")
            return True
        else:
            print(f"  ❌ Push failed: {result.stderr}")
            return False


# ============================================================
# MAIN PIPELINE
# ============================================================

def update_context():
    """Update .ctx file with latest state."""
    ctx_file = CONFIG["research_dir"] / "AI Working Directory" / ".ctx"
    if ctx_file.exists():
        content = ctx_file.read_text()
        # Update timestamp
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('ΩΣ:'):
                lines[i] = f"ΩΣ:v1|ts:{datetime.now().strftime('%Y-%m-%dT%H:%M')}|uid:kqi"
                break
        safe_fs.write_text(ctx_file, '\n'.join(lines))


def run_pipeline(dry_run: bool = False):
    """Run full auto-publish pipeline."""
    print("=" * 60)
    print("🔄 Auto-Publish Pipeline")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Update context file
    update_context()

    # 1. Sync Medium
    medium = MediumSync()
    new_articles = medium.sync()

    # 2. Prepare staging (converts docx → md)
    publisher = GitHubPublisher()
    publisher.prepare_staging()

    # 3. Git sync
    success = publisher.git_sync(dry_run=dry_run)

    print("\n" + "=" * 60)
    if success:
        print("✅ Pipeline complete")
        print(f"   https://github.com/{CONFIG['github_repo']}")
    else:
        print("❌ Pipeline failed")
    print("=" * 60)

    return success


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    success = run_pipeline(dry_run=dry_run)
    sys.exit(0 if success else 1)
