#!/usr/bin/env python3
"""
Regenerate papers/index.md from papers/index.json.

Usage:
    python scripts/rebuild_index_md.py

Run this any time index.json is updated (e.g. after a new search/download
session) to keep the human-readable table in sync.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = REPO_ROOT / "papers" / "index.json"
INDEX_MD = REPO_ROOT / "papers" / "index.md"


def load_papers() -> list[dict]:
    if not INDEX_JSON.exists():
        raise FileNotFoundError(f"No index.json found at {INDEX_JSON}")

    with open(INDEX_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Support either a flat list or a dict keyed by paper id
    if isinstance(data, dict):
        papers = list(data.values())
    else:
        papers = data

    return papers


def escape_md(text: str) -> str:
    """Escape pipe characters so titles/authors don't break the markdown table."""
    if not text:
        return ""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def format_row(paper: dict) -> str:
    title = escape_md(paper.get("title", "Untitled"))
    authors = escape_md(paper.get("authors", ""))
    year = paper.get("year", "")
    source = paper.get("source", "")
    doi_url = paper.get("doi") or paper.get("url") or ""
    tags = ", ".join(paper.get("tags", [])) if paper.get("tags") else ""
    pdf_path = paper.get("local_pdf_path", "")

    link = f"[{doi_url}]({doi_url})" if doi_url.startswith("http") else doi_url
    pdf_link = f"[PDF]({pdf_path})" if pdf_path else ""

    return f"| {title} | {authors} | {year} | {source} | {link} | {tags} | {pdf_link} |"


def build_markdown(papers: list[dict]) -> str:
    # Sort newest first; papers with missing/non-numeric year sort last
    def sort_key(p):
        try:
            return -int(p.get("year", 0))
        except (ValueError, TypeError):
            return 0

    papers_sorted = sorted(papers, key=sort_key)

    lines = [
        "# Paper Index",
        "",
        f"_{len(papers_sorted)} papers — auto-generated from `index.json`. Do not edit by hand._",
        "",
        "| Title | Authors | Year | Source | DOI/URL | Tags | PDF |",
        "|---|---|---|---|---|---|---|",
    ]
    lines.extend(format_row(p) for p in papers_sorted)

    # Optional: summaries section below the table
    lines.append("")
    lines.append("## Summaries")
    lines.append("")
    for p in papers_sorted:
        title = p.get("title", "Untitled")
        summary = p.get("summary", "_No summary available._")
        lines.append(f"### {title}")
        lines.append("")
        lines.append(summary)
        lines.append("")

    return "\n".join(lines)


def main():
    papers = load_papers()
    markdown = build_markdown(papers)
    INDEX_MD.write_text(markdown, encoding="utf-8")
    print(f"Wrote {len(papers)} papers to {INDEX_MD}")


if __name__ == "__main__":
    main()
