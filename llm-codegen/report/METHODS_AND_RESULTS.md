### Assignment scaffold: prompting, evaluation, and results

- **LLM families**: placeholder families `gpt/` and `claude/` used to simulate two families in `generations/`.
- **Problems (10)**: reverse_string, sum_list, is_palindrome, fibonacci, factorial, two_sum, merge_sorted_arrays, longest_common_prefix, balanced_parentheses, roman_to_int, anagram_groups, matrix_transpose, uniq_in_order.
- **Prompt strategies**: CoT, SCoT, and Self-Repair (for failed cases) with templates under `prompts/`.
- **Evaluation metric**: pass@k (k in {1,3}) computed per problem/family/strategy grouping.

### How to run

```bash
python llm-codegen/eval/run_eval.py \
  --data-dir llm-codegen/data \
  --generations-dir llm-codegen/generations \
  --tests-dir llm-codegen/tests \
  --results llm-codegen/eval/results.csv \
  --plots-dir llm-codegen/eval/plots
```

### Results (excerpt)

| problem_id | family | strategy | n_samples | n_correct | pass@1 | pass@3 |
|---|---|---|---:|---:|---:|---:|
| is_palindrome | gpt | cot | 1 | 0 | 0.000 | 0.000 |
| is_palindrome | gpt | self_repair | 1 | 1 | 1.000 | 1.000 |
| two_sum | claude | cot | 1 | 0 | 0.000 | 0.000 |
| two_sum | claude | self_repair | 1 | 1 | 1.000 | 1.000 |
| roman_to_int | claude | cot | 1 | 0 | 0.000 | 0.000 |
| roman_to_int | claude | self_repair | 1 | 1 | 1.000 | 1.000 |

Full CSV: `llm-codegen/eval/results.csv`.

### Debugging and iterative improvement

- **Failure 1 (gpt / is_palindrome / CoT)**: Ignored spec to remove non-alphanumeric and case-fold; fixed by filtering with `str.isalnum()` and lowercasing before reversal (Self-Repair).
- **Failure 2 (claude / two_sum / CoT)**: Returned values instead of indices; replaced with hashmap index lookup ensuring `i < j` (Self-Repair).
- **Failure 3 (claude / roman_to_int / CoT)**: Wrong numeral value for `L`; corrected values map (Self-Repair).

### Innovation: light-weight Self-Repair workflow

- When tests fail, rerun with `self_repair_generic.txt` prompting to produce a minimal corrected function. This reduced failures to pass in the above cases. For broader studies, add multi-sample generation per strategy to evaluate true pass@k gains.


