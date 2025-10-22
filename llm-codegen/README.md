### llm-codegen

A minimal scaffold for organizing LLM code generation experiments.

```text
llm-codegen/
  data/                 # problem IDs or your own NL specs
  prompts/              # *.txt templates per strategy
  generations/          # model/problem/strategy_sampleN.py
  tests/                # test_*.py per problem
  eval/                 # run_eval.py, results.csv, plots
  report/               # figures for the PDF
  README.md
```

### Directories
- **data/**: Input problem specs or identifiers used to drive generation.
- **prompts/**: Prompt templates (e.g., strategy-specific `.txt` files).
- **generations/**: Model outputs organized by `model/problem/` with versioned samples.
- **tests/**: Unit tests per problem (`test_*.py`).
- **eval/**: Evaluation utilities and outputs.
  - `run_eval.py`: Entry point to run evaluations.
  - `results.csv`: Aggregated evaluation results.
  - `plots/`: Generated figures from evaluations.
- **report/**: Final figures for inclusion in a report/PDF.

### Quick start
1) Put your problem specs in `data/` and your prompt templates in `prompts/`.
2) Generate candidate solutions into `generations/` (e.g., `modelX/problemY/strategy_A_sample1.py`).
3) Add tests in `tests/` (e.g., `test_problemY.py`).
4) Run evaluation via `eval/run_eval.py` and collect outputs in `eval/results.csv` and figures in `eval/plots/`.



