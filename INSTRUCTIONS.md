# Complete Guide: Exercise 1 with HumanEval+ Dataset

## Overview
This guide walks you through completing Exercise 1 using 10 diverse problems from the HumanEval+ dataset, evaluated with Gemini API and ChatGPT-5.

---

## Step 1: Set Up HumanEval+ Problems

### 1.1 Install Required Libraries
Open Windows CMD:
```cmd
cd /d D:\Umass\Semester_3\cs520\exercise_1
sat_env\Scripts\activate
pip install datasets huggingface_hub
```

### 1.2 Run Setup Script
```cmd
python setup_humaneval.py
```

This script will:
- Download HumanEval+ dataset (164 problems total)
- Select 10 diverse problems (easy/medium/hard):
  - HumanEval/0 (has_close_elements)
  - HumanEval/1 (separate_paren_groups)
  - HumanEval/10 (make_palindrome)
  - HumanEval/12 (longest)
  - HumanEval/17 (parse_music)
  - HumanEval/25 (factorize)
  - HumanEval/31 (is_prime)
  - HumanEval/54 (same_chars)
  - HumanEval/61 (correct_bracketing)
  - HumanEval/108 (count_nums)
- Create `llm-codegen/data/<problem_id>.json` for each
- Create `llm-codegen/tests/test_<problem_id>.py` for each
- Backup old custom problems to `llm-codegen/_old_custom_problems/`
- Clean `llm-codegen/generations/` folder

---

## Step 2: Set Up API Access

### 2.1 Gemini API
1. Go to https://aistudio.google.com/app/apikey
2. Create a new API key
3. Save it securely (you'll use it in generation scripts)

### 2.2 ChatGPT-5
1. Ensure you have access to ChatGPT-5 at https://chat.openai.com/
2. You'll manually copy-paste prompts and responses

---

## Step 3: Generate Solutions (Part 1)

You need to generate solutions for:
- 10 problems × 2 families (gpt, gemini) × 2 strategies (cot, scot) = 40 base files
- Optionally: up to 3 samples per combination for pass@3

### 3.1 Using ChatGPT-5 (Browser) - `gpt` family

For each problem in `llm-codegen/data/`:

1. Open the JSON file (e.g., `humaneval_0.json`)
2. Read the `description` field
3. Note the `function_name` field

**CoT Prompt Template:**
```
Task: Implement the target function in Python.

Chain-of-Thought:
1) Restate the contract and constraints.
2) Reason about edge cases and examples.
3) Identify a correct and simple algorithm.
4) Implement the function.

Output only the function implementation.

Problem:
<paste description here>

Function name: <function_name>
```

4. Paste into ChatGPT-5
5. Copy ONLY the function code (no explanations)
6. Save to: `llm-codegen/generations/humaneval_0/gpt/cot/cot_sample1.py`

**SCoT Prompt Template:**
```
Task: Implement the target function as specified.

Stepwise Chain-of-Thought Plan:
1) Restate the function contract precisely.
2) Identify edge cases and constraints.
3) Outline a step-by-step algorithm.
4) Implement the function in Python, adhering to the contract.
5) Double-check correctness on edge cases.

Output: Only the function implementation; no extra prints.

Problem:
<paste description here>

Function name: <function_name>
```

7. Save to: `llm-codegen/generations/humaneval_0/gpt/scot/scot_sample1.py`

**Repeat for all 10 problems**

### 3.2 Using Gemini API - `gemini` family

Create a generation script `generate_gemini.py`:

```python
import google.generativeai as genai
import json
from pathlib import Path

# Configure API
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

# Load prompt templates
cot_template = Path("llm-codegen/prompts/cot_generic.txt").read_text()
scot_template = Path("llm-codegen/prompts/scot_generic.txt").read_text()

# Generate for each problem
data_dir = Path("llm-codegen/data")
for data_file in sorted(data_dir.glob("*.json")):
    problem_data = json.loads(data_file.read_text())
    problem_id = problem_data["problem_id"]
    function_name = problem_data["function_name"]
    description = problem_data["description"]
    
    print(f"Generating for {problem_id}...")
    
    # CoT generation
    cot_prompt = f"{cot_template}\n\nProblem:\n{description}\n\nFunction name: {function_name}"
    response = model.generate_content(cot_prompt)
    
    # Save CoT
    cot_dir = Path(f"llm-codegen/generations/{problem_id}/gemini/cot")
    cot_dir.mkdir(parents=True, exist_ok=True)
    (cot_dir / "cot_sample1.py").write_text(response.text)
    
    # SCoT generation
    scot_prompt = f"{scot_template}\n\nProblem:\n{description}\n\nFunction name: {function_name}"
    response = model.generate_content(scot_prompt)
    
    # Save SCoT
    scot_dir = Path(f"llm-codegen/generations/{problem_id}/gemini/scot")
    scot_dir.mkdir(parents=True, exist_ok=True)
    (scot_dir / "scot_sample1.py").write_text(response.text)

print("Done!")
```

Run:
```cmd
sat_env\Scripts\activate
pip install google-generativeai
python generate_gemini.py
```

---

## Step 4: Run Evaluation

```cmd
sat_env\Scripts\activate
python llm-codegen\eval\run_eval.py ^
  --data-dir llm-codegen\data ^
  --generations-dir llm-codegen\generations ^
  --tests-dir llm-codegen\tests ^
  --results llm-codegen\eval\results.csv ^
  --plots-dir llm-codegen\eval\plots
```

Review results:
```cmd
type llm-codegen\eval\results.csv
```

---

## Step 5: Debug Failures (Part 2)

### 5.1 Identify Failures
Look for rows in `results.csv` where `n_correct < n_samples` or `pass@1 = 0.000`

### 5.2 Self-Repair Process
For each failure:

1. Open the failing `.py` file
2. Open the corresponding test file to see what failed
3. Use `llm-codegen/prompts/self_repair_generic.txt`:

```
You are given a failing function implementation and failing test feedback.

Goal: Produce a corrected implementation that fixes the described failures while preserving the contract.

Procedure:
- Diagnose the cause using the failing inputs/expected outputs.
- Propose a minimal, correct fix.
- Provide only the corrected function implementation; no prints.

Problem: <description>
Function name: <function_name>

Failing implementation:
<paste failing code>

Test case that failed:
<describe the failing test from test file>

Expected behavior:
<what should happen>
```

4. Generate fixed version with ChatGPT-5 or Gemini
5. Save to: `llm-codegen/generations/<problem_id>/<family>/self_repair/self_repair_sample1.py`
6. Re-run evaluation
7. Document in your report:
   - Original prompt
   - Failing code
   - Self-repair prompt
   - Fixed code
   - Analysis of why it failed

**Repeat for at least 2 failures**

---

## Step 6: Innovation Strategy (Part 3)

### 6.1 Design Novel Strategy
Create `llm-codegen/prompts/self_plan_feedback.txt`:

```
Task: Implement the target function with self-planning and validation.

Workflow:
1) Restate the problem contract and identify key constraints.
2) List 3-5 edge cases that must be handled correctly.
3) Outline your algorithm step-by-step.
4) Implement the function in Python.
5) Mentally trace through each edge case to verify correctness.
6) Output only the final validated function implementation.

Problem:
<description>

Function name: <function_name>
```

### 6.2 Generate with New Strategy
Generate for both families (gpt, gemini) across all 10 problems:
- Save to: `llm-codegen/generations/<problem_id>/<family>/self_plan_feedback/self_plan_feedback_sample1.py`

### 6.3 Evaluate
Re-run evaluation and compare pass@k vs CoT/SCoT

---

## Step 7: Write Report

Edit `llm-codegen/report/METHODS_AND_RESULTS.md`:

### Required Sections:

1. **LLM Families Used**
   - ChatGPT-5 (GPT family)
   - Gemini Pro (Gemini family)
   - Versions and access methods

2. **Problems Selected**
   - List 10 HumanEval+ problems with task IDs
   - Justify diversity (easy/medium/hard mix)

3. **Prompting Strategies**
   - CoT (paste exact prompt)
   - SCoT (paste exact prompt)
   - Self-Repair (paste exact prompt)
   - Innovation strategy (paste exact prompt)

4. **Experimental Setup**
   - Number of samples per strategy
   - Directory structure
   - Evaluation command

5. **Results (Part 1)**
   - Table from `results.csv`
   - pass@1 and pass@3 for each (problem, family, strategy)
   - Discussion of patterns

6. **Debugging Analysis (Part 2)**
   - At least 2 failure case studies
   - Before/after prompts and code
   - Why the model failed
   - How different families compare
   - Effectiveness of fixes

7. **Innovation Results (Part 3)**
   - Describe workflow
   - Comparative pass@k table
   - Analysis (why it worked/didn't work)
   - Differences across families

8. **GitHub Repository Link**
   - Include link to public repo

### Export to PDF:
- Use Markdown to PDF converter or copy to Word and export
- Name: `Exercise1.pdf`

---

## Step 8: Prepare GitHub Repository

### 8.1 Ensure Complete Structure:
```
llm-codegen/
  data/                    # 10 HumanEval+ problem JSONs
  prompts/                 # CoT, SCoT, Self-Repair, Innovation templates
  generations/             # All generated .py files
    <problem_id>/
      gpt/
        cot/, scot/, self_repair/, self_plan_feedback/
      gemini/
        cot/, scot/, self_repair/, self_plan_feedback/
  tests/                   # 10 test files
  eval/
    run_eval.py
    results.csv            # Final results
    plots/                 # Any plots generated
  report/
    METHODS_AND_RESULTS.md
Exercise1.pdf              # Final report
```

### 8.2 Push to GitHub:
```cmd
git add .
git commit -m "Complete Exercise 1 with HumanEval+ dataset"
git push origin main
```

---

## Step 9: Submit

1. Open `Exercise1.pdf`
2. Verify GitHub link is included
3. Submit to Gradescope before deadline (Oct 22, 11:59 PM EST)

---

## Quick Reference: Directory Structure

```
Problem: humaneval_0
Function: has_close_elements

Generations needed:
✓ llm-codegen/generations/humaneval_0/gpt/cot/cot_sample1.py
✓ llm-codegen/generations/humaneval_0/gpt/scot/scot_sample1.py
✓ llm-codegen/generations/humaneval_0/gemini/cot/cot_sample1.py
✓ llm-codegen/generations/humaneval_0/gemini/scot/scot_sample1.py
✓ llm-codegen/generations/humaneval_0/gpt/self_repair/self_repair_sample1.py (if failed)
✓ llm-codegen/generations/humaneval_0/gemini/self_repair/self_repair_sample1.py (if failed)
✓ llm-codegen/generations/humaneval_0/gpt/self_plan_feedback/self_plan_feedback_sample1.py
✓ llm-codegen/generations/humaneval_0/gemini/self_plan_feedback/self_plan_feedback_sample1.py
```

Repeat for all 10 problems!

---

## Troubleshooting

**Q: Test fails with "function not found"?**
A: Ensure the .py file defines the exact `function_name` from the JSON

**Q: Evaluation shows 0 samples?**
A: Check file naming: must be `<strategy>_sample1.py` in correct directory

**Q: Gemini API quota exceeded?**
A: Use free tier limits; add delays between requests if needed

**Q: Need more than 1 sample for pass@3?**
A: Generate `_sample2.py`, `_sample3.py` with same prompt (models give different outputs)

---

## Summary Checklist

- [ ] Install datasets library
- [ ] Run `setup_humaneval.py`
- [ ] Verify 10 problems in `data/` and `tests/`
- [ ] Get Gemini API key
- [ ] Generate 20 files (10 problems × 2 strategies) for `gpt` family
- [ ] Generate 20 files (10 problems × 2 strategies) for `gemini` family
- [ ] Run evaluation
- [ ] Debug ≥2 failures with self-repair (4+ files)
- [ ] Create innovation strategy prompt
- [ ] Generate with innovation (20 files: 10 problems × 2 families)
- [ ] Re-run evaluation
- [ ] Write METHODS_AND_RESULTS.md with all required sections
- [ ] Export to Exercise1.pdf
- [ ] Push to GitHub
- [ ] Submit to Gradescope

Good luck!

