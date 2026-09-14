# Taiwan Tech Conferences

> Open data for technology conferences held in Taiwan.

A simple, machine-readable dataset of technology conferences in Taiwan.

## API

https://goescat.github.io/Taiwan-Tech-Conferences/data/conferences.json

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
