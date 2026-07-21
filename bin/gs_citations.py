"""Fetch Google Scholar stats into assets/gs_data.json.

Run daily by .github/workflows/google-scholar-stats.yml, which commits the
refreshed file back to the site branch. The citation badge on the homepage
reads it same-origin, so the last known numbers keep showing even if a later
scrape fails (Google frequently blocks CI IP ranges).
"""

import json
import os
from datetime import datetime, timezone

from scholarly import scholarly

SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "9rqTLMcAAAAJ").strip()
OUT_PATH = os.path.join("assets", "gs_data.json")


def main():
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "counts"])

    citations = author.get("citedby")
    if not citations:
        raise SystemExit("no citation count returned — refusing to overwrite existing data")

    stats = {
        "citedby": citations,
        "hindex": author.get("hindex"),
        "i10index": author.get("i10index"),
        "cites_per_year": author.get("cites_per_year"),
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(stats, f, indent=2)
        f.write("\n")

    print(f"citations: {citations}, h-index: {stats['hindex']}")


if __name__ == "__main__":
    main()
