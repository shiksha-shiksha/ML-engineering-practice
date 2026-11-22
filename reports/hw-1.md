# HW-1

Здесь представлены выводы терминала при прогоне моего проекта перед коммитом.

## 1. Установка зависимостей

```bash
uv sync --locked
```

```
Resolved 35 packages in 1ms
Checked 31 packages in 0.72ms
```

## 2. Загрузка данных

```bash
uv run python -m src.get_data
```

```
Dataset successfully downloaded to data/raw/gallstone.csv
```

## 3. Pre-commit хуки

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

```
pre-commit installed at .git/hooks/pre-commit
```


```
check for added large files..............................................Passed
check for broken symlinks............................(no files to check)Skipped
detect destroyed symlinks................................................Passed
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
mixed line ending........................................................Passed
check yaml...............................................................Passed
check toml...............................................................Passed
check json...........................................(no files to check)Skipped
check for merge conflicts................................................Passed
detect private key.......................................................Passed
check for case conflicts.................................................Passed
ruff check...............................................................Failed
- hook id: ruff-check
- exit code: 1

E501 Line too long (93 > 88)
  --> src/train.py:12:89
   |
10 | filepath = "data/raw/gallstone.csv"
11 | if not Path(filepath).is_file():
12 |     raise FileNotFoundError(f"Dataset file not found: {filepath}. Run src/get_data.py first")
   |                                                                                         ^^^^^
13 |
14 | data = pd.read_csv(filepath)
   |

Found 1 error.

ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook

1 file reformatted, 2 files left unchanged
```

## 4. Повторный прогон

```bash
uv run ruff check
uv run ruff format --check .
```

```
All checks passed!
3 files already formatted
```

## 5. Обучение модели

```bash
uv run python -m src.train
```

```
Accuracy: 0.7969
```



## Скриншот со всеми соответствующими командами

![ml_eng_practice](/home/hoshicasia/Downloads/ml_eng_practice.jpg)
