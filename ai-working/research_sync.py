#!/usr/bin/env python3
"""
Research Sync - Unified Medium + GitHub Workflow
=================================================

A complete research workflow tool that:
1. Syncs Medium publications to local Markdown files
2. Audits content for PII/secrets before sharing
3. Publishes to GitHub with organized structure

Designed for researchers using Claude Code to iterate on publications.

Setup:
    export MEDIUM_USERNAME="your_medium_username"
    export GITHUB_REPO="username/repo-name"

    # Optional: customize paths
    export RESEARCH_DIR="/path/to/research"
    export SYNC_DIR="/path/to/sync/output"

Usage:
    python research_sync.py medium      # Sync Medium articles
    python research_sync.py audit       # Security audit
    python research_sync.py github      # Prepare for GitHub
    python research_sync.py all         # Full workflow

Dependencies:
    pip install feedparser html2text

Author: Kevin L. Qi
Repository: https://github.com/qikevinl/oni-research
License: MIT
"""

import os
import re
import sys
import json
import shutil
import hashlib
import fnmatch
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# ============================================================
# CONFIGURATION
# ============================================================

def get_config() -> Dict:
    """Load configuration from environment variables with sensible defaults."""
    home = Path.home()

    return {
        # Medium sync
        "medium_username": os.environ.get("MEDIUM_USERNAME", ""),
        "sync_dir": Path(os.environ.get("SYNC_DIR", home / "Research" / "SYNC" / "Medium")),

        # GitHub sync
        "github_repo": os.environ.get("GITHUB_REPO", ""),
        "research_dir": Path(os.environ.get("RESEARCH_DIR", home / "Research")),

        # Output
        "staging_dir": Path(os.environ.get("STAGING_DIR", home / "Research" / ".github_staging")),
    }


# ============================================================
# MEDIUM SYNC
# ============================================================

try:
    import feedparser
    import html2text
    MEDIUM_DEPS_AVAILABLE = True
except ImportError:
    MEDIUM_DEPS_AVAILABLE = False


class MediumSync:
    """Sync Medium publications to local Markdown files."""

    def __init__(self, username: str, sync_dir: Path):
        self.username = username.lstrip("@")
        self.sync_dir = sync_dir
        self.state_file = sync_dir / ".sync_state.json"

        if MEDIUM_DEPS_AVAILABLE:
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
        self.state_file.write_text(json.dumps(state, indent=2))

    def sanitize_filename(self, title: str) -> str:
        safe = re.sub(r'[<>:"/\\|?*\'\u2018\u2019\u201c\u201d\u2014\u2013]', '', title)
        safe = re.sub(r'\s+', ' ', safe).strip()
        return safe[:100]

    def fetch_articles(self) -> List:
        feed_url = f"https://medium.com/feed/@{self.username}"
        print(f"  Fetching: {feed_url}")

        feed = feedparser.parse(feed_url)
        if feed.bozo and not feed.entries:
            print(f"  Error: {feed.bozo_exception}")
            return []

        print(f"  Found {len(feed.entries)} articles")
        return feed.entries

    def article_to_markdown(self, entry: Dict) -> str:
        title = entry.get("title", "Untitled")
        published = entry.get("published", "")
        link = entry.get("link", "")
        tags = [tag.term for tag in entry.get("tags", [])]
        content_html = entry.get("content", [{}])[0].get("value", "") or entry.get("summary", "")

        content_md = self.h2t.handle(content_html).strip()

        return f"""---
title: "{title}"
date: {published}
url: {link}
tags: {tags}
synced: {datetime.now().isoformat()}
---

# {title}

{content_md}

---
*Originally published on [Medium]({link})*
"""

    def sync_article(self, entry: Dict, state: Dict) -> bool:
        title = entry.get("title", "Untitled")
        link = entry.get("link", "")
        article_id = hashlib.md5(link.encode()).hexdigest()[:12]

        if article_id in state["downloaded"]:
            return False

        print(f"  Syncing: {title[:50]}...")

        try:
            markdown = self.article_to_markdown(entry)

            published = entry.get("published_parsed")
            if published:
                date_str = datetime(published.tm_year, published.tm_mon, published.tm_mday).strftime("%Y-%m-%d")
            else:
                date_str = datetime.now().strftime("%Y-%m-%d")

            filename = f"{date_str} - {self.sanitize_filename(title)}.md"
            filepath = self.sync_dir / filename
            filepath.write_text(markdown, encoding="utf-8")

            print(f"  Saved: {filename}")
            state["downloaded"].append(article_id)
            return True

        except Exception as e:
            print(f"  Error: {e}")
            return False

    def sync(self) -> int:
        if not MEDIUM_DEPS_AVAILABLE:
            print("Error: Install dependencies: pip install feedparser html2text")
            return 0

        if not self.username:
            print("Error: MEDIUM_USERNAME not set")
            print("Run: export MEDIUM_USERNAME='your_username'")
            return 0

        print(f"\n📰 Medium Sync - @{self.username}")
        print(f"   Output: {self.sync_dir}")
        print("-" * 50)

        self.sync_dir.mkdir(parents=True, exist_ok=True)
        state = self.load_state()

        articles = self.fetch_articles()
        new_count = 0

        for entry in articles:
            if self.sync_article(entry, state):
                new_count += 1
                self.save_state(state)

        print(f"\n✅ Synced {new_count} new articles")
        return new_count


# ============================================================
# SECURITY AUDITOR
# ============================================================

EXCLUDED_PATTERNS = [
    # Secrets
    ".env", ".env.*", "*.pem", "*.key", "*.p12", "credentials*", "secrets*",
    "*_secret*", "*_key*", "api_key*", ".netrc", ".npmrc", ".pypirc",

    # Config
    ".git/", ".claude/", ".deepseek/", "*.local.json", "settings.local.*",

    # OS/Editor
    ".DS_Store", "Thumbs.db", "*.swp", ".idea/", ".vscode/",

    # Temp
    "*.tmp", ".tmp.*", "__pycache__/", "*.pyc", ".sync_state.json", "sync.log",

    # Google Drive
    ".tmp.drivedownload/", ".tmp.driveupload/", "*.gdoc", "*.gsheet",

    # Staging
    ".github_staging/",
]

SCANNABLE_EXTENSIONS = [
    ".py", ".js", ".ts", ".json", ".yaml", ".yml", ".md", ".txt",
    ".html", ".sh", ".sql", ".xml", ".csv", ".conf", ".cfg", ".ini",
]

PII_PATTERNS = {
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "phone_us": r'\b(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
    "ssn": r'\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b',
    "api_key": r'(?i)(api[_-]?key|secret[_-]?key|auth[_-]?token)\s*[=:]\s*["\']?[A-Za-z0-9_\-]{20,}',
    "aws_key": r'(?i)AKIA[0-9A-Z]{16}',
    "private_key": r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----',
    "password": r'(?i)(password|passwd|pwd)\s*[=:]\s*["\'][^"\']+["\']',
}

ALLOWED_PATTERNS = [
    r'@medium\.com', r'@anthropic\.com', r'@openai\.com', r'noreply@',
    r'example\.com', r'localhost', r'127\.0\.0\.1',
]


class SecurityAuditor:
    """Audit files for PII and sensitive content."""

    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.findings = []

    def is_excluded(self, path: Path, base_dir: Path) -> bool:
        rel_path = str(path.relative_to(base_dir))
        name = path.name

        for pattern in EXCLUDED_PATTERNS:
            if pattern.endswith("/"):
                if pattern.rstrip("/") in rel_path.split("/"):
                    return True
            elif "*" in pattern:
                if fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(rel_path, pattern):
                    return True
            elif name == pattern:
                return True
        return False

    def is_allowed(self, match: str) -> bool:
        return any(re.search(p, match, re.IGNORECASE) for p in ALLOWED_PATTERNS)

    def scan_file(self, filepath: Path) -> List[Dict]:
        findings = []
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return []

        for pii_type, pattern in PII_PATTERNS.items():
            for match in re.finditer(pattern, content):
                if not self.is_allowed(match.group()):
                    line_num = content[:match.start()].count('\n') + 1
                    severity = "HIGH" if pii_type in ["ssn", "private_key", "password", "aws_key"] else "MEDIUM"
                    findings.append({
                        "type": pii_type,
                        "file": str(filepath),
                        "line": line_num,
                        "severity": severity
                    })
        return findings

    def audit(self, directory: Path) -> Tuple[List[Path], List[Dict]]:
        safe_files = []
        all_findings = []

        print(f"\n🔍 Security Audit")
        print(f"   Scanning: {directory}")
        print("-" * 50)

        for filepath in directory.rglob("*"):
            if not filepath.is_file():
                continue

            if self.is_excluded(filepath, directory):
                continue

            if filepath.suffix.lower() in SCANNABLE_EXTENSIONS:
                findings = self.scan_file(filepath)
                if findings:
                    all_findings.extend(findings)
                    for f in findings:
                        print(f"  ⚠️  {f['severity']}: {f['type']} in {filepath.name}:{f['line']}")
                else:
                    safe_files.append(filepath)
            else:
                safe_files.append(filepath)

        self.findings = all_findings

        high_count = len([f for f in all_findings if f["severity"] == "HIGH"])
        print(f"\n{'✅' if high_count == 0 else '❌'} {len(safe_files)} safe files, {len(all_findings)} findings ({high_count} HIGH)")

        return safe_files, all_findings


# ============================================================
# GITHUB SYNC
# ============================================================

class GitHubSync:
    """Prepare and sync research to GitHub."""

    # Logical file tree structure
    STRUCTURE = {
        "articles": {
            "extensions": [".md"],
            "description": "Published articles and drafts",
            "subdirs": {
                "published": "Synced from Medium",
                "drafts": "Work in progress",
            }
        },
        "papers": {
            "extensions": [".docx", ".pdf"],
            "description": "Academic papers and technical documents",
        },
        "framework": {
            "extensions": [],
            "description": "ONI Framework documentation",
        },
        "tools": {
            "extensions": [".py", ".sh"],
            "description": "Utility scripts and automation",
        },
        "images": {
            "extensions": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
            "description": "Diagrams and visualizations",
        },
        "data": {
            "extensions": [".json", ".yaml", ".yml", ".csv"],
            "description": "Data files and configurations",
        },
    }

    def __init__(self, config: Dict):
        self.config = config
        self.auditor = SecurityAuditor(verbose=False)

    def prepare_staging(self, safe_files: List[Path]) -> Path:
        staging = self.config["staging_dir"]

        if staging.exists():
            shutil.rmtree(staging)
        staging.mkdir(parents=True)

        # Create structure
        for category in self.STRUCTURE:
            (staging / category).mkdir()

        # Categorize and copy files
        research_dir = self.config["research_dir"]

        for filepath in safe_files:
            ext = filepath.suffix.lower()
            rel_path = filepath.relative_to(research_dir)

            # Determine category
            category = "data"  # default
            for cat, info in self.STRUCTURE.items():
                if ext in info.get("extensions", []):
                    category = cat
                    break

            # Special handling for Medium synced articles
            if "SYNC/Medium" in str(filepath):
                dest = staging / "articles" / "published" / filepath.name
                dest.parent.mkdir(exist_ok=True)
            else:
                dest = staging / category / filepath.name

            shutil.copy2(filepath, dest)

        return staging

    def generate_readme(self) -> str:
        config = self.config
        return f'''# ONI Research Repository

> Organic Neural Interface (ONI) Framework - Security research for brain-computer interfaces

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-blueviolet)](https://claude.ai/claude-code)

## Overview

This repository contains research on neural interface security, including:

- **The ONI Framework**: A 14-layer security model extending OSI into biological territory
- **The Coherence Metric**: Mathematical framework for neural signal validation
- **Threat Analysis**: Attack vectors and defenses for brain-computer interfaces

## Repository Structure

```
├── articles/           # Published articles and drafts
│   ├── published/      # Synced from Medium
│   └── drafts/         # Work in progress
├── papers/             # Academic papers and technical documents
├── framework/          # ONI Framework documentation
├── tools/              # Utility scripts
│   └── research_sync.py  # Medium + GitHub sync tool
├── images/             # Diagrams and visualizations
└── data/               # Data files
```

## Quick Start

### Using the Research Sync Tool

This repository includes `research_sync.py`, a unified tool for:
- Syncing Medium publications to local Markdown
- Security auditing before publishing
- Organized GitHub publishing

```bash
# Install dependencies
pip install feedparser html2text

# Configure
export MEDIUM_USERNAME="your_username"
export GITHUB_REPO="username/repo-name"

# Sync Medium articles
python tools/research_sync.py medium

# Run security audit
python tools/research_sync.py audit

# Prepare for GitHub
python tools/research_sync.py github
```

## Using with Claude Code

This research workflow is designed to work with [Claude Code](https://claude.ai/claude-code). Here's how to replicate it:

### 1. Initial Setup

```bash
# Start Claude Code in your research directory
cd ~/Research
claude

# Ask Claude to set up the workflow
> "Help me set up a research workflow with Medium sync and GitHub publishing"
```

### 2. Writing Articles

Claude Code can help you:
- Draft articles based on your research notes
- Maintain consistent writing style across publications
- Generate technical diagrams and pseudocode
- Create both Medium-friendly and academic paper versions

Example prompt:
```
> "Help me write a Medium article about [topic] following the ONI series style"
```

### 3. Research Iteration

The workflow supports iterative research:

1. **Capture Ideas**: Store notes in your research directory
2. **Draft Content**: Use Claude Code to expand notes into articles
3. **Sync & Publish**: Run `research_sync.py` to sync Medium and GitHub
4. **Iterate**: Claude Code reads your published work for context on future pieces

### 4. Security-First Publishing

The sync tool automatically:
- Scans for PII (emails, phone numbers, API keys)
- Excludes sensitive files (.env, credentials, private keys)
- Audits before any GitHub push
- Reports findings with severity levels

## Articles

| Date | Title | Link |
|------|-------|------|
| 2026-01-17 | Neural Ransomware Isn't Science Fiction | [Medium](https://medium.com/@qikevinl/neural-ransomware-isnt-science-fiction) |
| 2026-01-16 | Your Brain Has a Spam Filter | [Medium](https://medium.com/@qikevinl/your-brain-has-a-spam-filter-can-we-reverse-engineer-it) |
| 2026-01-16 | Your Brain Needs a Firewall | [Medium](https://medium.com/@qikevinl/your-brain-needs-a-firewall-heres-what-it-would-look-like) |
| 2026-01-15 | The OSI of Mind: Securing Human-AI Interfaces | [Medium](https://medium.com/@qikevinl/the-osi-of-mind-securing-human-ai-interfaces) |

## The ONI Framework

A 14-layer security model for neural interfaces:

- **Layers 1-7**: Traditional OSI (Physical → Application)
- **Layers 8-10**: Neural Interface Domain (Electrodes, LFP, Oscillations)
- **Layers 11-14**: Cognitive Domain (Memory, Attention, Executive, Identity)

### The Coherence Metric

Signal validation formula:

```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
```

Where:
- σ²φ = Phase variance (timing jitter)
- σ²τ = Transport variance (pathway reliability)
- σ²γ = Gain variance (amplitude stability)

## Contributing

This research is open for critique and collaboration:

- **Neuroscientists**: Challenge the biological assumptions
- **Security Engineers**: Find attack vectors I've missed
- **Ethicists**: Identify governance gaps

Open an issue or reach out on [Medium](https://medium.com/@qikevinl).

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgements

- Writing assistance: Claude Code (Anthropic)
- Visualization assistance: ChatGPT (OpenAI)

All ideas, analyses, and conclusions are the author's own.

---

*The brain's firewall won't build itself.*
'''

    def prepare(self) -> bool:
        print(f"\n📦 GitHub Sync")
        print(f"   Repository: {self.config['github_repo'] or 'Not configured'}")
        print("-" * 50)

        # Audit first
        safe_files, findings = self.auditor.audit(self.config["research_dir"])

        high_severity = [f for f in findings if f["severity"] == "HIGH"]
        if high_severity:
            print(f"\n❌ Cannot proceed: {len(high_severity)} HIGH severity issues found")
            return False

        # Prepare staging
        print("\n  Preparing staging directory...")
        staging = self.prepare_staging(safe_files)

        # Write README
        (staging / "README.md").write_text(self.generate_readme())

        # Write LICENSE
        (staging / "LICENSE").write_text("""MIT License

Copyright (c) 2026 Kevin L. Qi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")

        # Copy this script to tools/
        tools_dir = staging / "tools"
        tools_dir.mkdir(exist_ok=True)
        shutil.copy2(__file__, tools_dir / "research_sync.py")

        print(f"\n✅ Staging ready: {staging}")
        print(f"   Files prepared: {sum(1 for _ in staging.rglob('*') if _.is_file())}")

        return True


# ============================================================
# MAIN CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Research Sync - Unified Medium + GitHub Workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  medium    Sync Medium publications to local Markdown
  audit     Run security audit on research directory
  github    Prepare research for GitHub publishing
  all       Run full workflow (medium → audit → github)

Examples:
  %(prog)s medium                    # Sync Medium articles
  %(prog)s audit                     # Security audit only
  %(prog)s github                    # Prepare GitHub staging
  %(prog)s all                       # Full workflow

Environment Variables:
  MEDIUM_USERNAME   Your Medium username (without @)
  GITHUB_REPO       GitHub repo (username/repo-name)
  RESEARCH_DIR      Path to research directory
  SYNC_DIR          Path for Medium sync output
        """
    )

    parser.add_argument("command", choices=["medium", "audit", "github", "all"],
                        help="Command to run")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output")

    args = parser.parse_args()
    config = get_config()

    print("=" * 60)
    print("Research Sync - Unified Medium + GitHub Workflow")
    print("=" * 60)

    if args.command in ["medium", "all"]:
        syncer = MediumSync(config["medium_username"], config["sync_dir"])
        syncer.sync()

    if args.command in ["audit", "all"]:
        auditor = SecurityAuditor(verbose=True)
        auditor.audit(config["research_dir"])

    if args.command in ["github", "all"]:
        gh_sync = GitHubSync(config)
        if gh_sync.prepare():
            print("\n" + "=" * 60)
            print("NEXT STEPS")
            print("=" * 60)
            print(f"""
1. Authenticate GitHub CLI (if not already):
   gh auth login

2. Create and push repository:
   cd {config['staging_dir']}
   git init
   git add .
   git commit -m "Initial research publication"
   gh repo create {config['github_repo'] or 'your-username/oni-research'} --public --source=. --push

Or for existing repo:
   git remote add origin https://github.com/{config['github_repo'] or 'your-username/oni-research'}.git
   git push -u origin main
""")


if __name__ == "__main__":
    main()
