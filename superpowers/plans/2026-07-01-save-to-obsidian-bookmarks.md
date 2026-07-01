# Save-to-Obsidian Bookmarks Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a per-item "💾 Save to Obsidian" link to the daily digest that creates a rich note in the user's Obsidian vault via the `obsidian://` URL scheme.

**Architecture:** A new pure helper module (`src/services/obsidian.py`) builds an `obsidian://new?...` URI and note body from a `ContentItem`. `DailySummarizer` gains an optional `ObsidianConfig` and, when present, appends the link (as a raw HTML anchor) to each item block in `_format_item`. The orchestrator passes `config.obsidian` into the summarizer. No backend, no JavaScript, no Obsidian plugins.

**Tech Stack:** Python 3, Pydantic v2 (`BaseModel`), pytest, `urllib.parse`, `hashlib`.

## Global Constraints

- The feature is **opt-in**: when `config.obsidian` is `None` (or `enabled=False`), rendering is byte-for-byte unchanged. No new required config.
- New config field mirrors the existing `email`/`webhook` optional pattern: `obsidian: Optional[ObsidianConfig] = None` on `Config`.
- Default note folder: `News/Horizon` (vault-relative).
- Filename: `<slug>-<hash>` where `<hash>` = first 8 hex chars of `sha256(str(item.url))`. **Never** use Obsidian's `overwrite` param.
- The link is emitted as a **raw HTML anchor** (`<a href="obsidian://...">`), not a markdown link, to avoid kramdown mangling the non-standard scheme.
- Both `file` and `content` URI params are fully URL-encoded via `urllib.parse.quote(value, safe="")`.
- Follow existing code style in `src/` (type hints, no new dependencies — everything used is stdlib or already imported).

---

### Task 1: Add `ObsidianConfig` model and wire into `Config`

**Files:**
- Modify: `src/models.py` (add `ObsidianConfig` after `EmailConfig` at line 361; add field to `Config` at line 391)
- Test: `tests/test_models_obsidian.py` (create)

**Interfaces:**
- Produces: `ObsidianConfig(vault: str, folder: str = "News/Horizon", enabled: bool = True)` and `Config.obsidian: Optional[ObsidianConfig] = None`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_models_obsidian.py`:

```python
"""Tests for the optional Obsidian bookmark config."""

from src.models import Config, ObsidianConfig


def _base_config_dict() -> dict:
    return {
        "ai": {"provider": "openai", "model": "gpt-4o", "api_key_env": "OPENAI_API_KEY"},
        "sources": {},
        "filtering": {},
    }


def test_config_defaults_obsidian_to_none():
    cfg = Config.model_validate(_base_config_dict())
    assert cfg.obsidian is None


def test_obsidian_config_defaults():
    data = _base_config_dict()
    data["obsidian"] = {"vault": "Obsidian"}
    cfg = Config.model_validate(data)
    assert cfg.obsidian is not None
    assert cfg.obsidian.vault == "Obsidian"
    assert cfg.obsidian.folder == "News/Horizon"
    assert cfg.obsidian.enabled is True


def test_obsidian_config_overrides():
    obs = ObsidianConfig(vault="MyVault", folder="Clips", enabled=False)
    assert obs.vault == "MyVault"
    assert obs.folder == "Clips"
    assert obs.enabled is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_models_obsidian.py -v`
Expected: FAIL with `ImportError: cannot import name 'ObsidianConfig'` (or `AttributeError` on `cfg.obsidian`).

> Note: `AIConfig`/`SourcesConfig`/`FilteringConfig` may require different keys than the stub above. If validation fails on those (not on `obsidian`), adjust `_base_config_dict()` to satisfy the current `AIConfig` required fields — inspect `src/models.py:97` (`AIConfig`) and copy a minimal valid set. The `obsidian` assertions are what matter.

- [ ] **Step 3: Add the model**

In `src/models.py`, immediately after the `EmailConfig` class (ends at line 361), add:

```python
class ObsidianConfig(BaseModel):
    """Optional Obsidian bookmarking: render a Save link per digest item."""

    vault: str  # Obsidian vault name (as shown in Obsidian), used in obsidian:// URIs
    folder: str = "News/Horizon"  # vault-relative folder new notes are created in
    enabled: bool = True
```

Then add the field to the `Config` class (after `webhook` at line 391):

```python
    obsidian: Optional[ObsidianConfig] = None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_models_obsidian.py -v`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add src/models.py tests/test_models_obsidian.py
git commit -m "feat: add optional ObsidianConfig to Config model"
```

---

### Task 2: Create the `src/services/obsidian.py` helper module

**Files:**
- Create: `src/services/obsidian.py`
- Test: `tests/test_obsidian.py` (create)

**Interfaces:**
- Consumes: `ObsidianConfig` (Task 1), `ContentItem` (`src/models.py`).
- Produces:
  - `slugify_title(title: str, max_len: int = 80) -> str`
  - `build_note_body(item: ContentItem, language: str, date: str) -> str`
  - `build_save_uri(cfg: ObsidianConfig, item: ContentItem, language: str, date: str) -> str`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_obsidian.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_obsidian.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.services.obsidian'`.

- [ ] **Step 3: Write the module**

Create `src/services/obsidian.py`:

```python
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
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
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
            f"source: {source}",
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_obsidian.py -v`
Expected: PASS (8 passed).

- [ ] **Step 5: Commit**

```bash
git add src/services/obsidian.py tests/test_obsidian.py
git commit -m "feat: add obsidian save-uri / note-body builder"
```

---

### Task 3: Render the save link in `DailySummarizer`

**Files:**
- Modify: `src/ai/summarizer.py` (`typing` import line 4; `DailySummarizer.__init__` ~line 67; `generate_summary` → `_format_item` call at line 112; `_format_item` signature at line 163 and its trailing block ~lines 246-247)
- Test: `tests/test_summarizer.py` (extend)

**Interfaces:**
- Consumes: `build_save_uri` (Task 2), `ObsidianConfig` (Task 1).
- Produces: `DailySummarizer(obsidian: Optional[ObsidianConfig] = None)`; `_format_item(self, item, labels, language, index, date: Optional[str] = None)` gains a trailing optional `date`.

**⚠️ Critical — two callers of `_format_item`:**
`_format_item` is called from **both** `generate_summary` (line 112) **and** `generate_webhook_item` (line 161: `return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")`). Therefore `date` **must** be optional (default `None`), and the save link **must** only render when `date is not None`. This (a) keeps `generate_webhook_item`'s existing call working unchanged, and (b) deliberately keeps the `obsidian://` link out of webhook output (the link is only for the web/email digest, per spec). Only update the line-112 caller; leave line 161 exactly as-is.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_summarizer.py`:

```python
from src.models import ObsidianConfig


def test_generate_summary_includes_save_link_when_obsidian_configured():
    summarizer = DailySummarizer(obsidian=ObsidianConfig(vault="Obsidian"))
    result = _run_async(
        summarizer.generate_summary(
            [_make_item(1)], date="2026-07-01", total_fetched=10, language="en"
        )
    )
    assert "obsidian://new?" in result
    assert "Save to Obsidian" in result


def test_generate_summary_omits_save_link_when_obsidian_absent():
    summarizer = DailySummarizer()
    result = _run_async(
        summarizer.generate_summary(
            [_make_item(1)], date="2026-07-01", total_fetched=10, language="en"
        )
    )
    assert "obsidian://new?" not in result


def test_generate_summary_omits_save_link_when_obsidian_disabled():
    summarizer = DailySummarizer(obsidian=ObsidianConfig(vault="Obsidian", enabled=False))
    result = _run_async(
        summarizer.generate_summary(
            [_make_item(1)], date="2026-07-01", total_fetched=10, language="en"
        )
    )
    assert "obsidian://new?" not in result
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_summarizer.py -k obsidian -v`
Expected: FAIL — `DailySummarizer()` does not accept `obsidian=` (`TypeError`), and no `obsidian://` in output.

- [ ] **Step 3: Update the constructor**

In `src/ai/summarizer.py`, replace the current constructor (line 67):

```python
    def __init__(self):
        pass
```

with:

```python
    def __init__(self, obsidian=None):
        # obsidian: Optional[ObsidianConfig]; when set (and enabled), a
        # "Save to Obsidian" link is appended to each rendered item.
        self.obsidian = obsidian
```

- [ ] **Step 4: Thread `date` into `_format_item` (optional param)**

First, add `Optional` to the typing import at line 4:

```python
from typing import List, Dict, Optional
```

Change the `_format_item` signature (line ~163) from:

```python
    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
```

to:

```python
    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int, date: Optional[str] = None) -> str:
```

Update **only** the `generate_summary` call site (line 112, the list comprehension building `parts`) from:

```python
        parts = [self._format_item(item, labels, language, i + 1) for i, item in enumerate(items)]
```

to:

```python
        parts = [self._format_item(item, labels, language, i + 1, date) for i, item in enumerate(items)]
```

**Do NOT change** the `generate_webhook_item` call at line 161 — it stays `self._format_item(item, labels, language, index)`, so `date` defaults to `None` there and no save link is added to webhook output.

- [ ] **Step 5: Append the save link inside `_format_item`**

In `_format_item`, locate the trailing block (currently line ~246-247):

```python
        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"
```

Replace it with:

```python
        if date is not None and self.obsidian is not None and self.obsidian.enabled:
            from ..services.obsidian import build_save_uri

            uri = build_save_uri(self.obsidian, item, language, date)
            label = "💾 保存到 Obsidian" if language == "zh" else "💾 Save to Obsidian"
            lines.append("")
            lines.append(f'<a href="{uri}">{label}</a>')

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"
```

The `date is not None` guard is what keeps the link out of `generate_webhook_item`'s output.

- [ ] **Step 6: Run tests to verify they pass**

Run: `python -m pytest tests/test_summarizer.py -v`
Expected: PASS (all existing tests + 3 new obsidian tests).

- [ ] **Step 7: Commit**

```bash
git add src/ai/summarizer.py tests/test_summarizer.py
git commit -m "feat: render Save to Obsidian link in daily digest items"
```

---

### Task 4: Wire the orchestrator and document the config

**Files:**
- Modify: `src/orchestrator.py` (line 149 and line 707 — the two `DailySummarizer()` constructions)
- Modify: `docs/configuration.md` (add `obsidian` section)

**Interfaces:**
- Consumes: `Config.obsidian` (Task 1), `DailySummarizer(obsidian=...)` (Task 3).

- [ ] **Step 1: Pass the config at both construction sites**

In `src/orchestrator.py`, change the summarizer construction at line ~149:

```python
                summarizer = DailySummarizer()
```

to:

```python
                summarizer = DailySummarizer(obsidian=self.config.obsidian)
```

And at line ~707 (inside `_generate_summary`):

```python
        summarizer = DailySummarizer()
```

to:

```python
        summarizer = DailySummarizer(obsidian=self.config.obsidian)
```

- [ ] **Step 2: Verify the wiring imports cleanly and the full suite passes**

Run: `python -c "import src.orchestrator"`
Expected: no output, exit code 0 (no ImportError / syntax error).

Run: `python -m pytest -q`
Expected: whole suite PASSES (no regressions).

- [ ] **Step 3: Document the config**

In `docs/configuration.md`, add a new section (place it near the existing `email` / `webhook` documentation):

````markdown
### `obsidian` (optional)

Adds a **💾 Save to Obsidian** link to every item in the daily digest. Clicking
it opens your local Obsidian and creates a note for that item via the
`obsidian://` URL scheme. No plugins required. Omit this block to disable the
feature entirely.

```json
"obsidian": {
  "vault": "Obsidian",
  "folder": "News/Horizon",
  "enabled": true
}
```

| Field | Default | Description |
|-------|---------|-------------|
| `vault` | *(required)* | Your Obsidian vault name, exactly as shown in Obsidian. |
| `folder` | `News/Horizon` | Vault-relative folder new notes are created in. |
| `enabled` | `true` | Set to `false` to keep the config but stop rendering the link. |

Each saved item becomes its own note named `<slug>-<hash>.md`, with YAML
frontmatter (`title`, `url`, `source`, `score`, `tags`, `saved`) plus the AI
summary. The link works when reading the digest in a desktop browser; in email
clients `obsidian://` links are typically inert.
````

- [ ] **Step 4: Commit**

```bash
git add src/orchestrator.py docs/configuration.md
git commit -m "feat: wire ObsidianConfig into orchestrator + document it"
```

---

## Self-Review

**1. Spec coverage:**
- Config `ObsidianConfig` + optional field → Task 1. ✓
- `src/services/obsidian.py` with `slugify_title` / `build_note_body` / `build_save_uri` → Task 2. ✓
- Summarizer `__init__(obsidian=)`, `_format_item` raw-HTML anchor before `---`, `date` threading → Task 3. ✓
- Orchestrator passes `self.config.obsidian` at both sites → Task 4. ✓
- Note format (frontmatter + heading + summary), one-file-per-item, `<slug>-<hash>`, no overwrite → Task 2. ✓
- Email caveat → documented in Task 4 docs. ✓
- Tests (slugify, uri, body, `_format_item` include/omit/disabled) → Tasks 1-3. ✓
- Docs in `configuration.md` → Task 4. ✓
- Out-of-scope items (sync, saved page, un-save, Pocket/Notion) → not implemented, correct. ✓

**2. Placeholder scan:** No TBD/TODO/"handle edge cases"/"write tests for above". All steps carry real code. ✓ (Task 1 Step 2 note about `AIConfig` required fields is guidance for a real, expected environment difference, not a placeholder.)

**3. Type consistency:**
- `build_save_uri(cfg, item, language, date)` — same 4-arg signature in Task 2 definition, Task 2 tests, and Task 3 call site. ✓
- `_format_item(self, item, labels, language, index, date=None)` — `date` optional; `generate_summary` caller (line 112) updated to pass it, `generate_webhook_item` caller (line 161) intentionally left unchanged. Link gated on `date is not None`. ✓
- `ObsidianConfig(vault, folder="News/Horizon", enabled=True)` — consistent across Tasks 1-4. ✓
- `slugify_title(title, max_len=80)` — consistent between module and tests. ✓
