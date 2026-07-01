# Save-to-Obsidian Bookmarks — Design

**Date:** 2026-07-01
**Status:** Approved (design), pending implementation plan

## Problem

While reading the daily brief, the user finds items worth keeping but has no way
to save or bookmark them. The brief is delivered as a **static Jekyll site on
GitHub Pages** (plus optional email/webhook). There is no interactive backend, so
a "save" action cannot store state server-side.

## Decisions (from brainstorming)

- **Reading surface:** the GitHub Pages site, in a browser.
- **Where saves live:** sent to a tool the user already uses — **Obsidian**.
- **Note structure:** **one note per saved item**.
- **Entry content:** **rich** (title link, score, source, date, tags, AI summary).

## Approach

Add a **`💾 Save to Obsidian`** control to each item block in the daily digest.
Because Obsidian registers the `obsidian://` URL scheme, the control is just a
hyperlink: clicking it opens the user's local Obsidian and creates a note via the
built-in `obsidian://new?...` action.

Consequences:

- **No JavaScript, no backend, no third-party service, no Obsidian plugins** — it
  works on the static site exactly as it is today.
- The link is built at digest-generation time in `_format_item`
  (`src/ai/summarizer.py`), where the item's title, URL, AI summary, score, and
  tags are all already available.
- The feature is **opt-in** via config. With no config present, no link is
  rendered — upstream and other users are unaffected.

## Components

### 1. Config — `src/models.py`

New optional model mirroring `EmailConfig` / `WebhookConfig`:

```python
class ObsidianConfig(BaseModel):
    vault: str                            # e.g. "Obsidian"
    folder: str = "News/Horizon"          # vault-relative folder for notes
    enabled: bool = True
```

Added to `Config`:

```python
obsidian: Optional[ObsidianConfig] = None
```

Users add an `obsidian` block to `config.personal.json`. The detected vault on
this machine is `/Users/kunwu/Obsidian`, so `vault: "Obsidian"`.

### 2. New module — `src/services/obsidian.py`

Isolated, pure (no I/O), independently testable. Three functions:

- `slugify_title(title: str) -> str`
  Sanitize a title into a safe filename: strip characters illegal in Obsidian/OS
  filenames (`/ \ : * ? " < > |`), collapse whitespace to hyphens/spaces, strip
  leading dots, truncate to ~80 chars. Must handle CJK titles and empty/degenerate
  titles (fall back to a placeholder).

- `build_note_body(item: ContentItem, language: str, date: str) -> str`
  Produce the rich markdown note body with YAML frontmatter (see "Note format").
  `date` is the digest date, used for the `saved:` frontmatter field.

- `build_save_uri(cfg: ObsidianConfig, item: ContentItem, language: str, date: str) -> str`
  Compose the final `obsidian://new?vault=...&file=...&content=...` string, with
  `file` and `content` URL-encoded. Filename per "Filename / idempotency".

### 3. Summarizer integration — `src/ai/summarizer.py`

- `DailySummarizer.__init__(self, obsidian: Optional[ObsidianConfig] = None)` —
  store the config (currently the constructor takes no arguments).
- The orchestrator passes `self.config.obsidian` at both construction sites
  (`src/orchestrator.py:149` and `:707`).
- In `_format_item`, immediately before the trailing `---` (currently
  `summarizer.py:246-247`), append the save link **as a raw HTML anchor** when
  `self.obsidian` is set and `enabled`:

  ```html
  <a href="obsidian://new?...">💾 Save to Obsidian</a>
  ```

  Raw HTML (the file already emits raw `<a>`/`<details>` tags) avoids any risk of
  kramdown mangling or dropping the non-standard `obsidian://` scheme that a
  markdown-link `[label](obsidian://...)` might hit.
- `generate_summary` already receives the digest `date`; thread it into
  `_format_item` so the save-URI builder can stamp the `saved:` frontmatter field.

## Note format (one file per item, rich)

Path: `<folder>/<slug>-<hash>.md`, e.g. `News/Horizon/anthropic-ships-claude-opus-4-8-a1b2c3d4.md`

```markdown
---
title: "Anthropic ships Claude Opus 4.8"
url: https://example.com/article
source: reddit · r/ClaudeAI
score: 8.5
tags: [ai, anthropic, models]
saved: 2026-07-01
---
# [Anthropic ships Claude Opus 4.8](https://example.com/article)
⭐️ 8.5/10 · reddit · r/ClaudeAI · Jul 01

<AI summary text here>
```

Frontmatter makes the saved notes queryable later (e.g. via Dataview) without
committing to any such feature now.

## Filename / idempotency

Filename = `slugify_title(title)` + `"-"` + short hash of the item URL
(e.g. first 8 hex chars of a SHA-256 of `str(item.url)`).

- The hash prevents two different articles with the same title from colliding.
- Re-saving the same item resolves to the same filename.
- Use Obsidian's default create behavior (**no `overwrite`**). Worst case, a
  double-click produces a harmless `…-hash 1.md`. **Nothing the user has edited is
  ever overwritten.**

## Known caveat

The link is embedded in the shared summary markdown, which is also used for the
**email** digest. In email clients, `obsidian://` links are typically inert (and
pointless on mobile). This is expected and acceptable: the user reads on the web,
where the link works. Not worth special-casing the email path.

## Testing

- New `tests/test_obsidian.py`:
  - `slugify_title`: illegal characters, over-length, CJK, empty/whitespace-only.
  - `build_save_uri`: correct scheme and params, proper URL-encoding of `file` and
    `content`, folder respected.
  - `build_note_body`: frontmatter fields populated; missing optional fields
    (e.g. no tags, no summary) handled gracefully.
- Extend `tests/test_summarizer.py`:
  - `_format_item` includes the anchor when an `ObsidianConfig` is provided.
  - `_format_item` omits it when config is `None` or `enabled=False`.

## Docs

Add the `obsidian` config block (with field descriptions) to
`docs/configuration.md`.

## Out of scope (YAGNI)

Deliberately excluded from this design:

- Cross-device sync of saved items.
- A "saved items" page rendered on the GitHub Pages site.
- Un-saving / removing bookmarks from the UI.
- Read-later service integrations (Pocket, Raindrop, Instapaper).
- Notion integration.

The Obsidian vault *is* the saved list; managing it happens in Obsidian.
