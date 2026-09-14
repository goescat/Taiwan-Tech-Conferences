# 🇹Taiwan Tech Conferences

> Open data for technology conferences held in Taiwan.

A simple, machine-readable dataset of technology conferences in Taiwan.

## Data

The entire dataset lives in one file:

```text
data/
└── conferences.json
```

Example:

```json
[
  {
    "id": "coscup",
    "name": "COSCUP",
    "organizer": "COSCUP",
    "website": "https://coscup.org/",
    "editions": [
      {
        "year": 2026,
        "start_date": "2026-08-08",
        "end_date": "2026-08-09",
        "city": "Taipei",
        "venue": "National Taiwan University of Science and Technology",
        "link": "https://coscup.org/2026/en/"
      }
    ]
  }
]
```

There is deliberately no separate API-generation layer. The JSON file itself can be served as a static API.

## GitHub Pages

If this repository is published with GitHub Pages, the dataset is directly available at:

```text
https://<username>.github.io/taiwan-tech-conferences/data/conferences.json
```

Consumers can use it directly with `fetch()` or any HTTP client.

## Current seed data

The initial dataset contains 8 conferences:

- COSCUP
- HITCON
- PyCon Taiwan
- Hello World Dev Conference
- DevOpsDays Taipei
- MOPCON
- TCSE
- SITCON

This is a seed dataset, not a claim of completeness.

## Data quality

Run the validation script before submitting changes:

```bash
python scripts/validate.py
```

Validation checks duplicate conference IDs, duplicate edition years, and date ordering.

## License

Dataset: CC BY 4.0  
Code: MIT
