# Pokemon TCG AI

An AI agent for the Pokemon Trading Card Game competition.

## Setup

```bash
pip install -r requirements.txt
```

## Running

```bash
python main.py
```

## Team Conventions

- `main.py` and `deck.csv` are the competition entry points — keep them clean.
- All reusable logic lives under `src/`.
- Training scripts go in `training/`, evaluation scripts in `evaluation/`.
- Use `notebooks/` for exploration only — no production code there.
- Large files (models, data) are gitignored; sync via GDrive.

## Submission

```bash
bash scripts/submit.sh
```
