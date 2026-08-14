#!/bin/bash
cd /home/aditya/Programming/Capstone/paper-archive

# Only commit if there are changes
if ! git diff-index --quiet HEAD --; then
  git add papers/pdfs/ papers/index.json papers/index.md
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
  git commit -m "Auto-commit: Downloaded papers and metadata updates [$TIMESTAMP]"
  git push origin main 2>&1 | grep -E "^(To|remote:|master|main|\s)" || true
  echo "✓ Committed and pushed at $TIMESTAMP"
else
  echo "No changes to commit at $(date '+%Y-%m-%d %H:%M:%S')"
fi
