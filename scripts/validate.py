import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "conferences.json"

items = json.loads(DATA.read_text(encoding="utf-8"))
ids = set()

for conference in items:
    conference_id = conference["id"]
    if conference_id in ids:
        raise SystemExit(f"duplicate conference id: {conference_id}")
    ids.add(conference_id)

    years = set()
    for edition in conference.get("editions", []):
        year = edition["year"]
        if year in years:
            raise SystemExit(f"duplicate edition year: {conference_id} {year}")
        years.add(year)

        start = date.fromisoformat(edition["start_date"])
        end = date.fromisoformat(edition["end_date"])
        if end < start:
            raise SystemExit(f"end_date before start_date: {conference_id} {year}")

print(f"Validation passed: {len(items)} conferences.")
