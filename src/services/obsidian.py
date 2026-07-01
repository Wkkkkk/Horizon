"""Build obsidian:// save URIs and note bodies for digest items.

Pure functions only (no I/O), so they are trivially unit-testable. Used by
DailySummarizer to render an optional "Save to Obsidian" link per item.
"""

from __future__ import annotations

import hashlib
import re
from urllib.parse import quote

from ..models import ContentItem, ObsidianConfig

# Characters illegal in Obsidian note names / common filesystems.
_ILLEGAL = re.compile(r'[\\/:*?"<>|#^\[\]]')
_WS = re.compile(r"\s+")


def slugify_title(title: str, max_len: int = 80) -> str:
    """Turn a title into a filesystem/Obsidian-safe slug."""
    text = _ILLEGAL.sub(" ", title or "")
    text = _WS.sub("-", text).strip("-.")
    text = text.lower()
    if len(text) > max_len:
        text = text[:max_len].rstrip("-.")
    return text or "untitled"


def _yaml_str(value: str) -> str:
    """Return a YAML-safe double-quoted scalar."""
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
    )
    return f'"{escaped}"'


def _format_source(item: ContentItem) -> str:
    parts = [item.source_type.value]
    meta = item.metadata or {}
    if meta.get("subreddit"):
        parts.append(f"r/{meta['subreddit']}")
    elif meta.get("feed_name"):
        parts.append(str(meta["feed_name"]))
    elif item.author:
        parts.append(item.author)
    return " · ".join(parts)


def _summary_for(item: ContentItem, language: str) -> str:
    meta = item.metadata or {}
    return (
        meta.get(f"detailed_summary_{language}")
        or meta.get("detailed_summary")
        or item.ai_summary
        or ""
    )


def _url_hash(item: ContentItem) -> str:
    return hashlib.sha256(str(item.url).encode("utf-8")).hexdigest()[:8]


def build_note_body(item: ContentItem, language: str, date: str) -> str:
    """Render the rich markdown note body (YAML frontmatter + heading + summary)."""
    title = item.title
    url = str(item.url)
    source = _format_source(item)
    summary = _summary_for(item, language)
    score_fm = item.ai_score if item.ai_score is not None else "null"
    score_disp = item.ai_score if item.ai_score is not None else "?"
    tags = ", ".join(_yaml_str(t) for t in (item.ai_tags or []))

    frontmatter = "\n".join(
        [
            "---",
            f"title: {_yaml_str(title)}",
            f"url: {url}",
            f"source: {_yaml_str(source)}",
            f"score: {score_fm}",
            f"tags: [{tags}]",
            f"saved: {date}",
            "---",
        ]
    )
    heading = f"# [{title}]({url})"
    subtitle = f"⭐️ {score_disp}/10 · {source}"
    return f"{frontmatter}\n{heading}\n{subtitle}\n\n{summary}\n"


def build_save_uri(
    cfg: ObsidianConfig, item: ContentItem, language: str, date: str
) -> str:
    """Build the obsidian://new URI that creates the note for `item`."""
    filename = f"{slugify_title(item.title)}-{_url_hash(item)}"
    file_path = f"{cfg.folder.strip('/')}/{filename}"
    content = build_note_body(item, language, date)
    return (
        "obsidian://new?"
        f"vault={quote(cfg.vault, safe='')}"
        f"&file={quote(file_path, safe='')}"
        f"&content={quote(content, safe='')}"
    )
