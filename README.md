# 📚 Research Paper Archive
## Adaptive Federated Learning for Distributed Video Anomaly Detection

A comprehensive research paper archive for capstone project on federated learning and video anomaly detection. Includes 280+ papers with 87 PDFs downloaded and indexed.

---

## 📊 Archive Statistics

### Overall Coverage
| Metric | Value |
|--------|-------|
| **Total Papers Indexed** | 280 |
| **Papers with PDFs** | 87 (31%) |
| **Total Storage** | 186 MB |
| **Last Updated** | 2026-08-15 |

### Papers by Source
| Source | Count | With PDF | Coverage |
|--------|-------|----------|----------|
| **arXiv** | 55 | 54 | 98.2% ✅ |
| **OpenAlex** | 77 | 17 | 22.1% |
| **CrossRef** | 68 | 10 | 14.7% |
| **DBLP** | 80 | 6 | 7.5% |

### Papers by Year (Recent)
| Year | Count | With PDF | Coverage |
|------|-------|----------|----------|
| **2027** | 13 | 3 | 23% |
| **2026** | 40 | 18 | 45% |
| **2025** | 40 | 13 | 32% |
| **2024** | 32 | 10 | 31% |
| **2023** | 31 | 14 | 45% |

---

## 🔍 Papers by Search Keyword

### Primary Keyword: "federated learning video anomaly detection"
- **Papers Found:** 280
- **PDFs Downloaded:** 87 (31%)
- **Search Date:** 2026-08-14
- **Sources Queried:** arXiv, CrossRef, OpenAlex, DBLP
- **Download Method:** Multi-source search + Unpaywall API

**Popular Tags:**
- `federated-learning` (106 papers)
- `anomaly-detection` (143 papers)
- `deep-learning` (81 papers)
- `edge-computing` (56 papers)
- `privacy-preserving` (50 papers)

### Other Keywords
*(To be added with additional searches)*

---

## 📁 Directory Structure

```
paper-archive/
├── README.md                          # This file
├── papers/
│   ├── index.json                     # Machine-readable archive (280 papers)
│   ├── index.md                       # Human-readable paper table
│   ├── pdfs/                          # Downloaded PDFs (87 files, 186 MB)
│   │   ├── federated-attention-autoencoders-with-a_arxiv_2608.08906v1.pdf
│   │   ├── advancing-network-anomaly-detection-using-deep-lea_crossref_10.5220_0013134100003928.pdf
│   │   └── ... (87 total PDFs)
│   └── aggregated_papers.json         # (deprecated - use index.json)
├── scripts/
│   └── auto-commit.sh                 # 5-minute auto-sync to GitHub
└── .gitignore                         # Excludes temp files

```

---

## 🚀 Quick Start

### Browse Papers
1. **Human-readable:** Open `papers/index.md` in your editor
   - Sorted by year (newest first)
   - Shows title, authors, source, tags, summary

2. **Machine-readable:** Use `papers/index.json`
   ```bash
   jq '.papers[] | select(.tags[] | contains("federated-learning"))' papers/index.json
   ```

### Download a Paper
All papers have either:
- **Local PDF:** `local_pdf_path` → file on disk
- **Online URL:** `url` → direct link to paper

### Statistics
```bash
# Count papers by tag
jq '.papers[] | .tags[]' papers/index.json | sort | uniq -c | sort -rn

# Find papers from a specific year
jq '.papers[] | select(.year == 2025)' papers/index.json

# Search by keyword in title/summary
jq '.papers[] | select(.title | contains("federated"))' papers/index.json
```

---

## 🔄 Adding More Searches

To expand the archive with additional keyword searches:

1. **Plan your search:**
   ```bash
   # Proposed keyword: "privacy-preserving machine learning"
   # Sources: arXiv, CrossRef, OpenAlex, DBLP
   # Target: 10-15 results per source = 50-60 papers
   ```

2. **Add to archive:**
   ```bash
   # Will deduplicate against existing 280 papers
   # Download new PDFs via Unpaywall
   # Update papers/index.json
   # Update README.md with new keyword stats
   ```

3. **Update this README:**
   - Add new keyword section below "Other Keywords"
   - Include: papers found, PDFs downloaded, key tags
   - Update overall statistics

---

## 📝 File Reference

### papers/index.json
**Format:** JSON with array of paper objects
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
      "summary": "3-5 sentence summary of paper...",
      "tags": ["federated-learning", "anomaly-detection", "deep-learning"],
      "abstract": "Full abstract text..."
    }
  ],
  "total": 280,
  "last_updated": "2026-08-15T00:46:00"
}
```

### papers/index.md
**Format:** Markdown table sorted by year
- Columns: Title, Authors, Year, Source, Tags, Summary
- Grouped by year (newest → oldest)
- 280 papers total

---

## 🔧 Automation

### Auto-Commit Loop
The repository auto-commits new PDFs and metadata every 5 minutes:
```bash
# Start manually:
./scripts/auto-commit.sh

# Or run loop:
nohup ./scripts/auto-commit-loop.sh &
```

### .gitignore Rules
Excludes from git:
- Temporary `.py` files
- `downloads/` directory
- Build artifacts
- IDE files

---

## 📋 Data Quality

- **280 papers:** Deduplicated by title/DOI
- **87 PDFs:** Verified > 1KB (successful downloads)
- **All papers:** Have title, authors, year, source, URL
- **231 papers:** Have DOI for citation
- **Coverage:** 31% PDF availability (limited by access restrictions)

---

## 📄 Citation

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

---

## 🎯 Use Cases

- **Literature Review:** Browse `papers/index.md` by year/keyword
- **Research Planning:** Query `papers/index.json` by tags
- **Full-Text Search:** Download PDFs locally, use your PDF reader
- **Citation Management:** Export to BibTeX using DOIs
- **Trend Analysis:** Analyze paper tags and topics by year

---

## ✅ Maintenance

**Last Update:** 2026-08-15
- 280 papers indexed
- 87 PDFs downloaded (31% coverage)
- Auto-commit loop active
- Repository clean and synced to GitHub

**Future Enhancements:**
- Add more keyword searches
- Attempt DOAJ API for journal articles
- Direct URL crawling for additional PDFs
- Author website searches for preprints

---

## 📚 For Your Capstone

This archive supports your capstone project:
- **Problem Domain:** Federated Learning + Video Anomaly Detection
- **Research Scope:** 280 peer-reviewed and preprint papers
- **PDF Access:** 87 full-text downloads (31%)
- **Metadata:** All papers have DOI/URL for direct access

Use `papers/index.md` for quick browsing, `papers/index.json` for programmatic analysis.

---

**Repository:** GitHub (auto-synced every 5 minutes)  
**Archive Size:** 186 MB (PDFs + metadata)  
**Last Synced:** Check via `git log --oneline`
