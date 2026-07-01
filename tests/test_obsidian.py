"""Tests for the Obsidian save-URI / note-body builders."""

from datetime import datetime, timezone
from urllib.parse import urlparse, parse_qs

from src.models import ContentItem, ObsidianConfig, SourceType
from src.services.obsidian import (
    slugify_title,
    build_note_body,
    build_save_uri,
)


def _make_item(idx: int = 1) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Important Item {idx}",
        url=f"https://example.com/items/{idx}",
        content="content",
        author="tester",
        published_at=datetime(2026, 4, 25, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 8.5
    item.ai_summary = f"Summary for item {idx}."
    item.ai_tags = ["AI", "News"]
    return item


def test_slugify_strips_illegal_chars():
    slug = slugify_title('A/B: "C" <D>? *E* |F|')
    for ch in '/\\:*?"<>|':
        assert ch not in slug
    assert slug  # non-empty


def test_slugify_truncates_to_max_len():
    slug = slugify_title("word " * 100, max_len=80)
    assert len(slug) <= 80


def test_slugify_empty_returns_placeholder():
    assert slugify_title("   ") == "untitled"
    assert slugify_title("///") == "untitled"


def test_slugify_keeps_cjk():
    slug = slugify_title("重要新闻")
    assert "重要新闻" in slug


def test_build_note_body_has_frontmatter_and_heading():
    body = build_note_body(_make_item(1), "en", "2026-07-01")
    assert body.startswith("---\n")
    assert 'title: "Important Item 1"' in body
    assert "url: https://example.com/items/1" in body
    assert "score: 8.5" in body
    assert "saved: 2026-07-01" in body
    assert "# [Important Item 1](https://example.com/items/1)" in body
    assert "Summary for item 1." in body


def test_build_note_body_handles_missing_tags_and_summary():
    item = _make_item(2)
    item.ai_tags = []
    item.ai_summary = None
    item.ai_score = None
    body = build_note_body(item, "en", "2026-07-01")
    assert "tags: []" in body
    assert "score: null" in body
    # must not crash and must still contain the heading
    assert "# [Important Item 2](https://example.com/items/2)" in body


def test_build_save_uri_structure_and_encoding():
    cfg = ObsidianConfig(vault="Obsidian", folder="News/Horizon")
    uri = build_save_uri(cfg, _make_item(1), "en", "2026-07-01")
    assert uri.startswith("obsidian://new?")
    q = parse_qs(urlparse(uri).query)
    assert q["vault"] == ["Obsidian"]
    assert q["file"][0].startswith("News/Horizon/important-item-1-")
    # 8-char hex hash suffix on the filename
    filename = q["file"][0].rsplit("/", 1)[-1]
    assert len(filename.rsplit("-", 1)[-1]) == 8
    # content decoded back contains the note body
    assert "title:" in q["content"][0]
    assert "https://example.com/items/1" in q["content"][0]


def test_build_save_uri_is_deterministic():
    cfg = ObsidianConfig(vault="Obsidian")
    item = _make_item(1)
    assert build_save_uri(cfg, item, "en", "2026-07-01") == build_save_uri(
        cfg, item, "en", "2026-07-01"
    )
