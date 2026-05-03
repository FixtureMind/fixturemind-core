# FixtureMind Core

FixtureMind is a football intelligence platform for opponent analysis, squad planning and recruitment.

## Core idea

FixtureMind helps clubs make better decisions before the season and before each match by combining:
- opponent analysis
- squad structure analysis
- recruitment recommendations
- contract and loan context
- budget-aware player shortlists

## First product modules

### 1. OpponentIQ
Opponent analysis engine:
- tactical patterns
- strengths and weaknesses
- set pieces
- card/foul profile
- substitutions timing analysis

### 2. Squad Room
Internal club squad planning:
- squad structure by position
- contract expiry tracking
- loans in and out
- age curve
- wage and affordability context

### 3. Recruitment Engine
Player discovery and ranking:
- fit-score by role and club DNA
- league and opponent-context fit
- salary-aware recommendations
- shortlist generation

## Initial target markets

- Poland: Ekstraklasa and 1 Liga
- Cyprus: pilot / experimental use case
- Central and Eastern Europe player recruitment markets

## Planned data sources

- StatsBomb Open Data
- FBref
- API-Football or Sportmonks
- Transfermarkt
- Capology

## Repository structure

- `fm_ingest/` — data loading from APIs and sources
- `fm_models/` — metrics, scoring models, opponent models
- `fm_reports/` — report generation
- `notebooks/` — R&D and exploration
- `data/raw/` — raw data
- `data/processed/` — transformed datasets
- `data/external/` — exported third-party data
- `docs/` — product docs and specs

## First build goal

Build a working prototype that can:
1. ingest football data
2. store team, player, match and event information
3. generate one opponent report
4. generate one squad planning table
5. produce one salary-aware shortlist for a position
