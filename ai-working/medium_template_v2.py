#!/usr/bin/env python3
"""
Medium Article Template v2 - Based on @qikevinl Writing Style Analysis
======================================================================

ANALYZED PATTERNS FROM PUBLISHED ARTICLES:
1. Hook: Visceral, "picture this" scenarios that create immediate tension
2. Structure: Problem -> Existing Solutions -> Gap -> Your Framework -> Technical Deep-dive -> Limitations -> CTA
3. Tone: Accessible yet technical, uses rhetorical questions, conversational asides
4. Formatting: **Bold** for key terms, code blocks for pseudocode, comparison tables
5. Series Integration: Links to related ONI framework articles
6. Consistent tags and Sub-Tags

WRITING STYLE SIGNATURES:
- Opening with relatable/scary scenario, not academic abstract
- "Here's the thing..." or "Here's what's fascinating..." transitions
- Numbered breakdowns (1. Timing, 2. Transport, 3. Amplitude)
- Honest limitations section ("The Catch")
- Specific CTAs for different audiences (neuroscientists, security engineers, etc.)
- Em dashes for emphasis — like this
- Italics for internal monologue or asides
- Questions that guide the reader: "What does this mean?" -> Answer

ARTICLE STRUCTURE (PROVEN FORMAT):
1. HOOK (50-100 words): Visceral scenario or striking fact
2. PROBLEM (150-200 words): Why current solutions fail
3. INSIGHT (100-150 words): Your unique angle/discovery
4. SOLUTION (300-500 words): Framework explanation with examples
5. TECHNICAL (200-400 words): Formulas, pseudocode, diagrams
6. WHY IT MATTERS (100-150 words): Real-world implications
7. THE CATCH (100-150 words): Honest limitations
8. BIGGER PICTURE (100-150 words): Connection to ONI framework
9. WHAT'S NEXT (100-150 words): CTAs for specific audiences

Usage:
    from medium_template_v2 import MediumArticle
    article = MediumArticle(config)
    article.generate()
"""

import json
import re
from pathlib import Path
from typing import List, Tuple

# Medium's section divider (three centered dots)
MEDIUM_DIVIDER = "\n\n· · ·\n\n"


# ============================================================
# TABLE HANDLING UTILITIES
# ============================================================

def parse_markdown_table(table_text: str) -> Tuple[List[str], List[List[str]]]:
    """
    Parse a markdown table into headers and rows.

    Args:
        table_text: Markdown table string with | delimiters

    Returns:
        Tuple of (headers list, rows list of lists)
    """
    lines = [line.strip() for line in table_text.strip().split('\n') if line.strip()]

    headers = []
    rows = []

    for i, line in enumerate(lines):
        # Skip separator line (contains only |, -, :, spaces)
        if re.match(r'^[\|\-:\s]+$', line):
            continue

        # Parse cells
        cells = [cell.strip() for cell in line.split('|')]
        # Remove empty first/last cells from leading/trailing |
        cells = [c for c in cells if c]

        if not headers:
            headers = cells
        else:
            rows.append(cells)

    return headers, rows


def to_ascii_table(headers: List[str], rows: List[List[str]], style: str = "box") -> str:
    """
    Convert headers and rows to an ASCII table.

    Args:
        headers: List of header strings
        rows: List of row lists
        style: "box" for box-drawing chars, "simple" for +|-

    Returns:
        ASCII table string
    """
    if not headers:
        return ""

    # Calculate column widths
    all_rows = [headers] + rows
    num_cols = len(headers)
    col_widths = []

    for col_idx in range(num_cols):
        max_width = 0
        for row in all_rows:
            if col_idx < len(row):
                max_width = max(max_width, len(str(row[col_idx])))
        col_widths.append(max_width + 2)  # padding

    if style == "box":
        # Unicode box-drawing characters
        h_line = "─"
        v_line = "│"
        tl, tr, bl, br = "┌", "┐", "└", "┘"
        t_down, t_up, t_left, t_right = "┬", "┴", "├", "┤"
        cross = "┼"
    else:
        # Simple ASCII
        h_line = "-"
        v_line = "|"
        tl = tr = bl = br = t_down = t_up = t_left = t_right = cross = "+"

    def make_border(left, mid, right):
        parts = [left]
        for i, w in enumerate(col_widths):
            parts.append(h_line * w)
            parts.append(mid if i < len(col_widths) - 1 else right)
        return "".join(parts)

    def make_row(cells):
        parts = [v_line]
        for i, w in enumerate(col_widths):
            cell = str(cells[i]) if i < len(cells) else ""
            parts.append(f" {cell:<{w-2}} ")
            parts.append(v_line)
        return "".join(parts)

    lines = []
    lines.append(make_border(tl, t_down, tr))
    lines.append(make_row(headers))
    lines.append(make_border(t_left, cross, t_right))

    for row in rows:
        lines.append(make_row(row))

    lines.append(make_border(bl, t_up, br))

    return "\n".join(lines)


def convert_markdown_tables_to_ascii(content: str, use_code_block: bool = True) -> str:
    """
    Find and convert all markdown tables in content to ASCII format.

    Args:
        content: Text that may contain markdown tables
        use_code_block: Wrap output in markdown code block

    Returns:
        Content with tables converted to ASCII
    """
    # Pattern to match markdown tables
    # Looks for lines starting with | and containing table structure
    table_pattern = re.compile(
        r'((?:^\|[^\n]+\|[ ]*\n)+)',
        re.MULTILINE
    )

    def replace_table(match):
        table_text = match.group(1)
        headers, rows = parse_markdown_table(table_text)

        if not headers:
            return table_text  # Not a valid table, return as-is

        ascii_table = to_ascii_table(headers, rows)

        if use_code_block:
            return f"\n```\n{ascii_table}\n```\n"
        return ascii_table

    return table_pattern.sub(replace_table, content)


def replace_dividers_with_medium_style(content: str) -> str:
    """
    Replace markdown dividers (---) with Medium's · · · divider.

    Args:
        content: Markdown content

    Returns:
        Content with Medium-style dividers
    """
    # Match --- or *** or ___ (common markdown hr patterns)
    # with optional whitespace around them
    divider_pattern = re.compile(r'\n\s*([-*_]){3,}\s*\n')
    return divider_pattern.sub(MEDIUM_DIVIDER, content)


def wrap_inline_math_for_medium(content: str) -> str:
    """
    Wrap inline mathematical symbols and formulas in backticks for Medium paste compatibility.

    Symbols inside code blocks are preserved as-is. Only inline occurrences are wrapped.

    Args:
        content: Markdown content with potential inline math symbols

    Returns:
        Content with inline math wrapped in backticks
    """
    # Common inline math patterns to wrap in backticks (outside code blocks)
    # These patterns find symbols NOT already in backticks or code blocks

    replacements = [
        # Multiplication symbol -> x (simple replacement for inline)
        (r'(?<!`)(\d+)×(?!`)', r'\1x'),
        # Arrow symbols in inline text (not in code blocks)
        (r'(?<![`\w])→(?![`\w])', '->'),
        (r'(?<![`\w])←(?![`\w])', '<-'),
        # Less than or equal / greater than or equal
        (r'(?<!`)(\w)\s*≤\s*(\w)(?!`)', r'`\1 <= \2`'),
        (r'(?<!`)(\w)\s*≥\s*(\w)(?!`)', r'`\1 >= \2`'),
    ]

    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    return content


# ============================================================
# CONFIGURATION TEMPLATE
# ============================================================

DEFAULT_CONFIG = {
    # Metadata
    "title": "",
    "subtitle": "",
    "tags": ["#Neuroscience", "#BrainComputerInterface", "#Cybersecurity", "#Neuralink", "#AI", "#ONI"],

    # Series info
    "series_name": "ONI (Organic Neural Firewall) Framework",
    "related_articles": [
        {"title": "The OSI of Mind: Securing Human-AI Interfaces", "url": "https://medium.com/@qikevinl/the-osi-of-mind-securing-human-ai-interfaces-3ca381b95c29"},
        {"title": "Your Brain Has a Spam Filter", "url": "https://medium.com/@qikevinl/your-brain-has-a-spam-filter-can-we-reverse-engineer-it-799da714238e"},
        {"title": "Your Brain Needs a Firewall", "url": "https://medium.com/@qikevinl/your-brain-needs-a-firewall-heres-what-it-would-look-like-87b46d292219"},
        {"title": "Neural Ransomware Isn't Science Fiction", "url": "https://medium.com/@qikevinl/neural-ransomware-isnt-science-fiction-e3f9efe4ffb1"},
    ],

    # Content sections (populated per article)
    "hook": "",
    "problem": {"heading": "The Problem", "content": ""},
    "insight": {"heading": "The Insight", "content": ""},
    "solution": {"heading": "The Solution", "content": "", "formula": None, "formula_explanation": None},
    "technical": {"heading": "How It Works", "content": "", "pseudocode": None},
    "implications": {"heading": "Why This Matters", "content": ""},
    "limitations": {"heading": "The Catch", "content": ""},
    "bigger_picture": {"heading": "Part of Something Larger", "content": ""},
    "cta": {
        "heading": "What's Next",
        "audiences": [
            {"role": "neuroscientist", "ask": "tell me what's wrong with the biological assumptions"},
            {"role": "security engineer", "ask": "tell me how you'd break this"},
            {"role": "ethicist", "ask": "tell me what governance gaps I'm missing"},
        ],
        "closing": "The brain's firewall is not optional. Let's build it right."
    },

    # Paper link (if applicable)
    "paper": {"title": None, "url": None},

    # Next article teaser
    "next_article": {"title": None, "teaser": None},
}


class MediumArticle:
    """Generate Medium articles in the @qikevinl style."""

    def __init__(self, config: dict):
        self.config = {**DEFAULT_CONFIG, **config}

    def _process_content(self, content: str) -> str:
        """
        Process content to convert markdown tables to ASCII and apply Medium formatting.

        Args:
            content: Raw markdown content

        Returns:
            Processed content with ASCII tables in code blocks and inline math wrapped
        """
        # Convert any markdown tables to ASCII format in code blocks
        content = convert_markdown_tables_to_ascii(content)
        # Wrap inline math symbols for Medium paste compatibility
        content = wrap_inline_math_for_medium(content)
        return content

    def to_markdown(self) -> str:
        """Generate article as Markdown with Medium-specific formatting."""
        c = self.config
        lines = []

        # Frontmatter
        lines.append("---")
        lines.append(f'title: "{c["title"]}"')
        lines.append(f'subtitle: "{c["subtitle"]}"')
        lines.append(f'tags: {json.dumps(c["tags"])}')
        lines.append("---")
        lines.append("")

        # Title
        lines.append(f"# {c['title']}")
        lines.append("")
        lines.append(f"*{c['subtitle']}*")
        lines.append("")

        # Hook (process for tables)
        lines.append(self._process_content(c["hook"]))
        lines.append("")
        lines.append("---")
        lines.append("")

        # Main sections
        for section_key in ["problem", "insight", "solution", "technical", "implications", "limitations", "bigger_picture"]:
            section = c.get(section_key, {})
            if section.get("content"):
                lines.append(f"## {section['heading']}")
                lines.append("")
                # Process section content for tables
                lines.append(self._process_content(section["content"]))

                # Formula if present
                if section.get("formula"):
                    lines.append("")
                    lines.append(f"> **{section['formula']}**")
                    if section.get("formula_explanation"):
                        lines.append("")
                        lines.append(f"*{section['formula_explanation']}*")

                # Pseudocode if present
                if section.get("pseudocode"):
                    lines.append("")
                    lines.append("```python")
                    lines.append(section["pseudocode"])
                    lines.append("```")

                lines.append("")
                lines.append("---")
                lines.append("")

        # Call to Action
        cta = c["cta"]
        lines.append(f"## {cta['heading']}")
        lines.append("")
        for audience in cta.get("audiences", []):
            lines.append(f"- If you're a **{audience['role']}**: {audience['ask']}")
        lines.append("")
        lines.append(f"*{cta['closing']}*")
        lines.append("")

        # Series note
        lines.append("---")
        lines.append("")
        lines.append(f"*This article is part of a series on the {c['series_name']}.*")
        lines.append("")

        # Related articles
        if c.get("related_articles"):
            lines.append("**Related articles:**")
            for article in c["related_articles"]:
                lines.append(f"- [{article['title']}]({article['url']})")
            lines.append("")

        # Next article teaser
        if c.get("next_article", {}).get("title"):
            lines.append(f"*Next: \"{c['next_article']['title']}\" — {c['next_article']['teaser']}*")
            lines.append("")

        # Paper link
        if c.get("paper", {}).get("url"):
            lines.append(f"**Read the full technical paper:** [{c['paper']['title']}]({c['paper']['url']})")
            lines.append("")

        # Tags
        lines.append(f"**Sub-Tags:** {' '.join(c['tags'])}")
        lines.append("")

        # Join all lines and replace --- dividers with Medium's · · · style
        result = "\n".join(lines)
        result = replace_dividers_with_medium_style(result)

        return result

    def save(self, output_dir: Path = None) -> Path:
        """Save article to markdown file."""
        if output_dir is None:
            output_dir = Path("/Users/mac/Research/AI Working Directory/Articles")
        output_dir.mkdir(parents=True, exist_ok=True)

        # Create filename from title (Blog- prefix per naming convention)
        safe_title = re.sub(r'[<>:"/\\|?*]', '', self.config["title"])
        safe_title = re.sub(r'\s+', '_', safe_title)[:50]
        filename = f"Blog-{safe_title}.md"

        filepath = output_dir / filename
        filepath.write_text(self.to_markdown())
        print(f"Article saved to: {filepath}")
        return filepath


# ============================================================
# STYLE GUIDE & WRITING PROMPTS
# ============================================================

STYLE_GUIDE = """
## @qikevinl Medium Writing Style Guide

### HOOK PATTERNS (Choose one):
1. **Scenario**: "Picture this — [visceral scenario that could happen]"
2. **Striking Fact**: "Here's something that should keep you up at night: [fact]"
3. **Contradiction**: "[Common belief]. [Why it's wrong/incomplete]"
4. **Question**: "[Provocative question]? The answer might surprise you."

### TRANSITION PHRASES:
- "Here's the thing..."
- "Here's what's fascinating..."
- "But here's where it gets interesting..."
- "The question I've been obsessively pondering..."
- "Let me be specific..."
- "This isn't hypothetical."

### LIMITATION PATTERNS:
- "This framework isn't bulletproof."
- "There's a catch (because there's always a catch)."
- "It's also not empirically validated — yet."
- "But here's why I'm publishing anyway: we need shared vocabulary."

### CTA STRUCTURE:
- Address 2-3 specific audiences by role
- Ask for specific, actionable feedback
- End with memorable closing line

### FORMATTING RULES:
- Use **bold** for key terms on first introduction
- Use *italics* for asides, internal monologue, or emphasis
- Use > blockquotes for key formulas or pullquotes
- Section dividers are auto-converted to Medium's · · · style
- Use numbered lists for sequential steps or components
- Keep paragraphs short (2-4 sentences max)
- Use rhetorical questions to guide reader

### TABLES (Auto-converted):
Markdown tables are automatically converted to ASCII format in code blocks:

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

Becomes:
```
┌──────────┬──────────┐
│ Header 1 │ Header 2 │
├──────────┼──────────┤
│ Cell 1   │ Cell 2   │
└──────────┴──────────┘
```
This preserves table formatting in Medium's code blocks (data-code-block-mode="1").

### COHERENCE METRIC FORMULA (Standard):
> **Cₛ = e^(−(σ²φ + σ²τ + σ²γ))**
- σ²φ = Phase variance (timing jitter)
- σ²τ = Transport variance (pathway reliability)
- σ²γ = Gain variance (amplitude stability)

### ONI FRAMEWORK LAYERS (Reference):
- Layers 1-7: Traditional OSI
- Layers 8-10: Neural interface domain
- Layers 11-14: Cognitive domain
"""


def print_style_guide():
    """Print the style guide for reference."""
    print(STYLE_GUIDE)


# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":
    # Example: Create a new article
    example_config = {
        "title": "Example Article Title",
        "subtitle": "A compelling subtitle that hooks the reader.",
        "hook": """Picture this — you're debugging a neural interface when you realize
something terrifying: the signals look normal, but they're not coming from where they should.

This isn't a thought experiment. It's the gap in current BCI security.""",
        "problem": {
            "heading": "The Problem",
            "content": "Current frameworks weren't designed for biological endpoints..."
        },
        # ... add other sections
    }

    # Print style guide
    print_style_guide()

    print("\n" + "="*60)
    print("Template ready. Import MediumArticle class to generate articles.")
    print("="*60)
