# Gallstone Classification

This project showcases training of a simple RF model to predict gallstone disease on table data.
Dataset concists of medical measurements and binary disease outcome, which is used as a target.

## Dataset

- **Name:** Gallstone
- **Source:** Kaggle [`yasserhessein/gallstone`](https://www.kaggle.com/datasets/yasserhessein/gallstone)
- **License (Kaggle):** CC BY-NC-SA 4.0
- **Original:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/1150/gallstone-1) (CC BY 4.0); Esen et al. (2024), https://doi.org/10.1097/md.0000000000037258

## Getting started & Installation

You need python 3.11 and [uv](https://docs.astral.sh/uv/).

Clone the repository:

```bash
git clone git@github.com:hoshicasia/ML_eng_practice.git
cd ML_eng_practice
```
Install dependencies from the lock file:

```bash
uv sync --locked
```
Download data:

```bash
uv run python -m src.get_data
```

The dataset will be saved to `data/raw/gallstone.csv`.

## Code checks

Install pre-commit hooks:

```bash
uv run pre-commit install
```

Run all checks:

```bash
uv run pre-commit run --all-files
```

Run Ruff:

```bash
uv run ruff check .
uv run ruff format --check .
```

## Model training

To train the model:

```bash
uv run python -m src.train
```

The script trains a simple RF using and evaluates accuracy of predictions.

Outputs:
- `artifacts/model.pkl` — trained model
- `artifacts/metrics.json` — evaluation metrics

## Reproducibility

To run the entire project from scratch:

```bash
uv sync --locked
uv run python -m src.get_data
uv run pre-commit run --all-files
uv run python -m src.train
```

## Report

You can find report showing execution results in reports/hw-1.md
