# Research Paper Archive
Adaptive Federated Learning for Distributed Video Anomaly Detection

A comprehensive research paper archive for capstone project on federated learning and video anomaly detection. Includes 87 downloaded PDFs with complete metadata.

## Archive Statistics

Overall Coverage
| Metric | Value |
|--------|-------|
| Papers with PDFs | 87 |
| Total Storage | 186 MB |
| Last Updated | 2026-08-15 |

Papers by Source (Downloaded Only)
| Source | Count | Coverage |
|--------|-------|----------|
| arXiv | 54 | 62% |
| OpenAlex | 17 | 19% |
| CrossRef | 10 | 11% |
| DBLP | 6 | 7% |

Papers by Year (Downloaded)
| Year | Count |
|------|-------|
| 2026 | 7 |
| 2025 | 13 |
| 2024 | 10 |
| 2023 | 14 |
| 2022 | 12 |

## Papers by Search Keyword

Primary Keyword: "federated learning video anomaly detection"
- Papers Found and Downloaded: 87
- Search Date: 2026-08-14
- Sources Searched: arXiv, CrossRef, OpenAlex, DBLP
- Download Method: Multi-source search + Unpaywall API

Popular Tags (in downloaded papers)
- anomaly-detection (58 papers)
- deep-learning (45 papers)
- federated-learning (42 papers)
- edge-computing (25 papers)
- privacy-preserving (18 papers)

Other Keywords
(To be added with additional searches)

## Directory Structure

```
paper-archive/
├── README.md                          # This file
├── papers/
│   ├── index.json                     # Complete metadata (280 indexed papers)
│   ├── index.md                       # Downloaded papers table (87 papers)
│   ├── pdfs/                          # Downloaded PDFs (87 files, 186 MB)
│   │   ├── federated-attention-autoencoders-with-a_arxiv_2608.08906v1.pdf
│   │   ├── advancing-network-anomaly-detection-using-deep-lea_crossref_10.5220_0013134100003928.pdf
│   │   └── ... (87 total PDFs)
│   └── aggregated_papers.json         # (deprecated - use index.json)
├── scripts/
│   └── auto-commit.sh                 # 5-minute auto-sync to GitHub
└── .gitignore                         # Excludes temp files
```

## Quick Start

Browse Papers
1. Human-readable: Open papers/index.md in your editor
   - Shows all 87 downloaded papers
   - Sorted by year (newest first)
   - Shows title, authors, source, tags

2. Machine-readable: Use papers/index.json
```bash
jq '.papers[] | select(.local_pdf_path != null) | select(.tags[] | contains("federated-learning"))' papers/index.json
```

Download a Paper
All 87 downloaded papers have:
- Local PDF: local_pdf_path -> file on disk
- Online URL: url -> direct link to paper

Statistics
```bash
# Count papers by tag
jq '.papers[] | select(.local_pdf_path != null) | .tags[]' papers/index.json | sort | uniq -c | sort -rn

# Find papers from a specific year
jq '.papers[] | select(.local_pdf_path != null) | select(.year == 2025)' papers/index.json

# Search by keyword in title
jq '.papers[] | select(.local_pdf_path != null) | select(.title | contains("federated"))' papers/index.json
```

## Adding More Searches

To expand the archive with additional keyword searches:

1. Plan your search:
```bash
# Proposed keyword: "privacy-preserving machine learning"
# Sources: arXiv, CrossRef, OpenAlex, DBLP
# Target: 10-15 results per source = 50-60 papers
```

2. Add to archive:
```bash
# Will deduplicate against existing papers
# Download new PDFs via Unpaywall
# Update papers/index.json
# Update README.md with new keyword stats
```

3. Update this README:
   - Add new keyword section below "Other Keywords"
   - Include: papers downloaded, key tags
   - Update overall statistics

## File Reference

papers/index.md
Format: Markdown table with downloaded papers only
- Columns: Title, Authors, Year, Source, Tags
- Grouped by year (newest to oldest)
- 87 papers total

papers/index.json
Format: JSON with array of all papers (280 total)
```json
{
  "papers": [
    {
      "id": "arxiv_2608.08906",
      "title": "Federated Attention Autoencoders...",
      "authors": ["Author 1", "Author 2"],
      "year": 2026,
      "doi": "10.1109/...",
      "url": "http://arxiv.org/abs/2608.08906v1",
      "source": "arxiv",
      "local_pdf_path": "papers/pdfs/federated-attention-autoencoders-with-a_arxiv_2608.08906v1.pdf",
      "summary": "3-5 sentence summary...",
      "tags": ["federated-learning", "anomaly-detection"],
      "abstract": "Full abstract text..."
    }
  ],
  "total": 280,
  "last_updated": "2026-08-15T00:46:00"
}
```

## Automation

Auto-Commit Loop
The repository auto-commits new PDFs and metadata every 5 minutes:
```bash
# Start manually:
./scripts/auto-commit.sh

# Or run loop:
nohup ./scripts/auto-commit-loop.sh &
```

.gitignore Rules
Excludes from git:
- Temporary .py files
- downloads/ directory
- Build artifacts
- IDE files

## Data Quality

- 87 PDFs: Verified > 1KB (successful downloads)
- All PDFs: Have title, authors, year, source, URL
- All PDFs: Have tags for categorization
- 81 PDFs: Have DOI for citation
- All PDFs: Have local file path and metadata

## Citation

Use DOI when available:
```bibtex
@article{Example2026,
  author = {First Author and Second Author},
  title = {Paper Title},
  journal = {Journal Name},
  year = {2026},
  doi = {10.1234/example.doi}
}
```

Or use direct URL:
```
Author, "Title", Source, Year. URL: [link]
```

## Use Cases

- Literature Review: Browse papers/index.md by year/keyword
- Research Planning: Query papers/index.json by tags
- Full-Text Search: Download PDFs locally, use your PDF reader
- Citation Management: Export to BibTeX using DOIs
- Trend Analysis: Analyze paper tags and topics by year

## Maintenance

Last Update: 2026-08-15
- 87 PDFs downloaded and indexed
- Auto-commit loop active
- Repository clean and synced to GitHub

## For Your Capstone

This archive supports your capstone project:
- Problem Domain: Federated Learning + Video Anomaly Detection
- Papers Available: 87 full-text downloads
- Metadata: All papers have DOI/URL for direct access

Use papers/index.md for quick browsing, papers/index.json for programmatic analysis.

Repository: GitHub (auto-synced every 5 minutes)
Archive Size: 186 MB (PDFs + metadata)
Last Synced: Check via git log --oneline
