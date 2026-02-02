#!/usr/bin/env python3
"""
Medium RSS to Markdown Sync
============================

Automatically sync your Medium publications to local Markdown files.
Ideal for backup, AI/LLM context, or static site generation.

Setup:
    1. Set environment variable: export MEDIUM_USERNAME="your_username"
    2. Optionally set: export MEDIUM_SYNC_DIR="/path/to/output"
    3. Run: python medium_sync.py

Dependencies:
    pip install feedparser html2text

Features:
    - Fetches articles from your Medium RSS feed
    - Converts to clean Markdown with YAML frontmatter
    - Tracks synced articles to avoid duplicates
    - Safe filenames with date prefixes

Author: Kevin L. Qi
License: MIT
"""

import os
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime

try:
    import feedparser
except ImportError:
    print("Error: feedparser not installed. Run: pip install feedparser")
    exit(1)

try:
    import html2text
except ImportError:
    print("Error: html2text not installed. Run: pip install html2text")
    exit(1)


def get_config():
    """Load configuration from environment variables."""
    username = os.environ.get("MEDIUM_USERNAME")
    if not username:
        print("Error: MEDIUM_USERNAME environment variable not set.")
        print("Usage: export MEDIUM_USERNAME='your_username'")
        exit(1)

    sync_dir = os.environ.get("MEDIUM_SYNC_DIR", str(Path.home() / "Medium"))

    return {
        "username": username.lstrip("@"),
        "sync_dir": Path(sync_dir),
        "state_file": Path(sync_dir) / ".sync_state.json"
    }


# HTML to Markdown converter
h2t = html2text.HTML2Text()
h2t.ignore_links = False
h2t.ignore_images = False
h2t.body_width = 0  # No line wrapping


def load_state(state_file: Path) -> dict:
    """Load sync state to track already downloaded articles."""
    if state_file.exists():
        return json.loads(state_file.read_text())
    return {"downloaded": []}


def save_state(state: dict, state_file: Path):
    """Save sync state."""
    state_file.write_text(json.dumps(state, indent=2))


def sanitize_filename(title: str) -> str:
    """Convert title to safe filename."""
    # Remove/replace unsafe characters
    safe = re.sub(r'[<>:"/\\|?*\'\u2018\u2019\u201c\u201d\u2014\u2013]', '', title)
    safe = re.sub(r'\s+', ' ', safe).strip()
    return safe[:100]  # Limit length


def fetch_articles(username: str) -> list:
    """Fetch articles from Medium RSS feed."""
    feed_url = f"https://medium.com/feed/@{username}"
    print(f"Fetching: {feed_url}")

    feed = feedparser.parse(feed_url)

    if feed.bozo and not feed.entries:
        print(f"Error fetching feed: {feed.bozo_exception}")
        return []

    print(f"Found {len(feed.entries)} articles")
    return feed.entries


def article_to_markdown(entry: dict) -> str:
    """Convert feed entry to Markdown with YAML frontmatter."""
    title = entry.get("title", "Untitled")
    published = entry.get("published", "")
    link = entry.get("link", "")
    tags = [tag.term for tag in entry.get("tags", [])]
    content_html = entry.get("content", [{}])[0].get("value", "") or entry.get("summary", "")

    # Convert HTML content to Markdown
    content_md = h2t.handle(content_html).strip()

    # Build frontmatter + content
    md = f"""---
title: "{title}"
date: {published}
url: {link}
tags: {tags}
---

# {title}

{content_md}

---
*Originally published on [Medium]({link})*
"""
    return md


def download_article(entry: dict, state: dict, sync_dir: Path) -> bool:
    """Download and convert a single article to Markdown."""
    title = entry.get("title", "Untitled")
    link = entry.get("link", "")

    # Create unique ID from link
    article_id = hashlib.md5(link.encode()).hexdigest()[:12]

    if article_id in state["downloaded"]:
        print(f"  Skip: {title[:50]}...")
        return False

    print(f"  Sync: {title[:50]}...")

    try:
        markdown = article_to_markdown(entry)

        # Generate filename with date
        published = entry.get("published_parsed")
        if published:
            date_str = datetime(
                published.tm_year,
                published.tm_mon,
                published.tm_mday
            ).strftime("%Y-%m-%d")
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")

        filename = f"{date_str} - {sanitize_filename(title)}.md"
        filepath = sync_dir / filename

        filepath.write_text(markdown, encoding="utf-8")

        print(f"  Saved: {filename}")
        state["downloaded"].append(article_id)
        return True

    except Exception as e:
        print(f"  Error: {e}")
        return False


def sync():
    """Main sync function."""
    config = get_config()

    print(f"Medium Sync - @{config['username']}")
    print(f"Output: {config['sync_dir']}")
    print("-" * 50)

    # Ensure directory exists
    config['sync_dir'].mkdir(parents=True, exist_ok=True)

    # Load state
    state = load_state(config['state_file'])

    # Fetch and process articles
    articles = fetch_articles(config['username'])
    new_count = 0

    for entry in articles:
        if download_article(entry, state, config['sync_dir']):
            new_count += 1
            save_state(state, config['state_file'])

    print("-" * 50)
    print(f"Done. {new_count} new articles synced.")


if __name__ == "__main__":
    sync()
