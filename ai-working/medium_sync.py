#!/usr/bin/env python3
"""Sync Medium publications to Markdown files."""

import os
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime

import feedparser
import html2text

# Configuration
MEDIUM_USERNAME = "qikevinl"
SYNC_DIR = Path("/Users/mac/Research/SYNC/Medium")
STATE_FILE = SYNC_DIR / ".sync_state.json"

# HTML to Markdown converter
h2t = html2text.HTML2Text()
h2t.ignore_links = False
h2t.ignore_images = False
h2t.body_width = 0  # No wrapping

def load_state():
    """Load sync state to track already downloaded articles."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"downloaded": []}

def save_state(state):
    """Save sync state."""
    STATE_FILE.write_text(json.dumps(state, indent=2))

def sanitize_filename(title):
    """Convert title to safe filename."""
    safe = re.sub(r'[<>:"/\\|?*]', '', title)
    safe = re.sub(r'\s+', ' ', safe).strip()
    return safe[:100]

def fetch_articles():
    """Fetch articles from Medium RSS feed."""
    feed_url = f"https://medium.com/feed/@{MEDIUM_USERNAME}"
    print(f"Fetching feed: {feed_url}")

    feed = feedparser.parse(feed_url)

    if feed.bozo and not feed.entries:
        print(f"Error fetching feed: {feed.bozo_exception}")
        return []

    print(f"Found {len(feed.entries)} articles")
    return feed.entries

def article_to_markdown(entry):
    """Convert feed entry to Markdown."""
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

def download_article(entry, state):
    """Download and convert a single article to Markdown."""
    title = entry.get("title", "Untitled")
    link = entry.get("link", "")

    article_id = hashlib.md5(link.encode()).hexdigest()[:12]

    if article_id in state["downloaded"]:
        print(f"  Skipping (already synced): {title}")
        return False

    print(f"  Syncing: {title}")

    try:
        markdown = article_to_markdown(entry)

        # Generate filename with date
        published = entry.get("published_parsed")
        if published:
            date_str = datetime(published.tm_year, published.tm_mon, published.tm_mday).strftime("%Y-%m-%d")
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")

        filename = f"{date_str} - {sanitize_filename(title)}.md"
        filepath = SYNC_DIR / filename

        filepath.write_text(markdown)

        print(f"  Saved: {filename}")
        state["downloaded"].append(article_id)
        return True

    except Exception as e:
        print(f"  Error: {e}")
        return False

def sync():
    """Main sync function."""
    print(f"Medium Sync - @{MEDIUM_USERNAME}")
    print(f"Output: {SYNC_DIR}")
    print("-" * 50)

    SYNC_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()

    articles = fetch_articles()
    new_count = 0

    for entry in articles:
        if download_article(entry, state):
            new_count += 1
            save_state(state)

    print("-" * 50)
    print(f"Done. {new_count} new articles synced.")

if __name__ == "__main__":
    sync()
