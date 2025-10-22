# Exercise 1 - Quick Start Guide (Gemini + DeepSeek)

## ✅ What's Already Done

Setup is complete! Here's what's ready:

### 📁 10 HumanEval+ Problems Extracted
- `llm-codegen/data/` - 10 JSON files with problem specs
- `llm-codegen/tests/` - 10 test files with HumanEval+ test cases
- Old custom problems backed up to `llm-codegen/_old_custom_problems/`

### 📝 Problems Selected (Easy to Medium difficulty):
1. **humaneval_0** - has_close_elements (check if two numbers are close)
2. **humaneval_1** - separate_paren_groups (parse parentheses groups)
3. **humaneval_10** - make_palindrome (create palindrome from string)
4. **humaneval_12** - longest (find longest string in list)
5. **humaneval_17** - parse_music (convert music notation to integers)
6. **humaneval_25** - factorize (find prime factors)
7. **humaneval_31** - is_prime (check if number is prime)
8. **humaneval_54** - same_chars (check if two strings have same characters)
9. **humaneval_61** - correct_bracketing (validate bracket pairs)
10. **humaneval_108** - count_nums (count numbers with positive digit sum)

### 🛠️ Scripts Ready:
- ✅ `generate_with_gemini.py` - Auto-generate with Gemini API (20 files already done!)
- ✅ `generate_with_mistral.py` - Auto-generate with Mistral AI API
- ✅ `llm-codegen/eval/run_eval.py` - Evaluation script

### 🎯 LLM Families:
- **Gemini 2.5 Flash** (Google DeepMind) - API
- **Mistral Large** (Mistral AI) - API

---

## 🚀 What You Need to Do

### Step 1: Generate Solutions with Gemini API (Already Done! ✓)

The Gemini generation is complete! 20 files created:
- ✅ 10 problems × 2 strategies (CoT + SCoT) = 20 files in `gemini/` folders

If you need to regenerate:
```cmd
cd /d D:\Umass\Semester_3\cs520\exercise_1
set GEMINI_API_KEY=your_key_here
python generate_with_gemini.py
```

---

### Step 2: Generate Solutions with Mistral AI API (3-5 minutes)

1. Get API key from https://console.mistral.ai/ (Free tier available)

2. Open CMD and run:
```cmd
cd /d D:\Umass\Semester_3\cs520\exercise_1
set MISTRAL_API_KEY=your_actual_key_here
pip install mistralai
python generate_with_mistral.py
```

This generates 20 files:
- 10 problems × 2 strategies (CoT + SCoT) = 20 files in `mistral/` folders

**Total so far: 40 generation files**

---

### Step 3: Run Evaluation (1 minute)

```cmd
cd /d D:\Umass\Semester_3\cs520\exercise_1
python llm-codegen\eval\run_eval.py
type llm-codegen\eval\results.csv
```

This creates `results.csv` with pass@1 and pass@3 for each (problem, family, strategy).

You'll see results for both **gemini** and **mistral** families!

---

### Step 4: Debug Failures with Self-Repair (30 minutes)

1. Look at `results.csv` - find at least 2 rows where `pass@1 = 0.000`

2. For each failure:
   - Open the failing `.py` file
   - Open the test file `tests/test_humaneval_X.py`
   - Read `prompts/self_repair_generic.txt` for the template
   - Use either Gemini or DeepSeek API to generate a fix
   - Save to: `llm-codegen/generations/humaneval_X/<family>/self_repair/self_repair_sample1.py`

3. Re-run evaluation to verify fixes

**Add: ~4 files (2 failures × 2 families or attempts)**

---

### Step 5: Create Innovation Strategy (1 hour)

1. Create new prompt: `llm-codegen/prompts/your_strategy.txt`

Example innovation - "Self-Plan with Validation":
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

IMPORTANT: Output ONLY the Python function code. No explanations.
```

2. Generate for all 10 problems × 2 families (gemini, mistral):
   - Use either API or modify the generation scripts
   - Save to: `llm-codegen/generations/humaneval_X/gemini/your_strategy/your_strategy_sample1.py`
   - Save to: `llm-codegen/generations/humaneval_X/mistral/your_strategy/your_strategy_sample1.py`

3. Re-run evaluation and compare pass@k vs CoT/SCoT

**Add: 20 files (10 problems × 2 families)**

---

### Step 6: Write Report (2-3 hours)

Edit `llm-codegen/report/METHODS_AND_RESULTS.md`:

#### Required sections:

1. **LLM Families**
   - Gemini 2.5 Flash (Google DeepMind family) - API access via `models/gemini-2.5-flash`
   - Mistral Large (Mistral AI family) - API access via `mistral-large-latest`

2. **Problems** 
   - List 10 HumanEval+ problems with task IDs
   - Justify selection (easy/medium mix, diverse algorithms)
   - Source: https://huggingface.co/datasets/evalplus/humanevalplus

3. **Prompts**
   - Paste exact CoT prompt (from `prompts/cot_generic.txt`)
   - Paste exact SCoT prompt (from `prompts/scot_generic.txt`)
   - Paste exact Self-Repair prompt (from `prompts/self_repair_generic.txt`)
   - Paste exact Innovation prompt (your new one)

4. **Experimental Setup**
   - Directory structure: `generations/<problem>/<family>/<strategy>/`
   - Number of samples per strategy (1 per combo for pass@1)
   - Generation method: API calls for both families
   - Evaluation command: `python llm-codegen/eval/run_eval.py`

5. **Results (Part 1)**
   - Table from `results.csv`
   - pass@1 and pass@3 for gemini vs mistral
   - Discussion: Which family performed better? Where did they differ?

6. **Debugging (Part 2)**
   - 2+ failure case studies
   - Before/after code snippets
   - Exact prompts used for repair
   - Analysis: Why did it fail? Why does the fix work?
   - Comparison: How did Gemini vs Mistral handle the same failure?

7. **Innovation (Part 3)**
   - Describe your novel strategy
   - Workflow/rationale
   - Results table comparing your strategy vs CoT/SCoT
   - Analysis: Did it improve results? Why or why not?
   - Differences across Gemini vs Mistral

8. **GitHub Repository Link**
   - Include your public repo URL

#### Export to PDF:
- Use Markdown to PDF converter or copy to Word
- Name: `Exercise1.pdf`
- Save in repo root

---

### Step 7: Submit (5 minutes)

1. Push to GitHub:
```cmd
git add .
git commit -m "Complete Exercise 1 with Gemini + Mistral on HumanEval+"
git push origin main
```

2. Verify repo has:
   - `llm-codegen/data/` (10 JSONs)
   - `llm-codegen/tests/` (10 test files)
   - `llm-codegen/prompts/` (4 prompt files: CoT, SCoT, Self-Repair, Innovation)
   - `llm-codegen/generations/` (64+ .py files)
   - `llm-codegen/eval/results.csv`
   - `Exercise1.pdf`
   - `README.md`

3. Submit `Exercise1.pdf` to Gradescope
   - Deadline: Oct 22, 11:59 PM EST
   - Include GitHub link in the PDF

---

## 📊 File Count Summary

| Category | Files | Status |
|----------|-------|--------|
| Data (problems) | 10 | ✅ Done |
| Tests | 10 | ✅ Done |
| Prompts | 3+1 | ✅ Done (CoT, SCoT, Self-Repair) + Add Innovation |
| Gemini generations | 20 | ✅ Already generated! |
| Mistral generations | 20 | ⏳ Run `generate_with_mistral.py` |
| Self-repair | 4+ | ⏳ After evaluation |
| Innovation | 20 | ⏳ New strategy |
| **Total generations** | **64+** | |

---

## ⚡ Time Estimate

- Gemini generation: ✅ Done! (5 min)
- Mistral generation: 5 min
- First evaluation: 1 min
- Self-repair: 30 min
- Innovation: 1 hour
- Report writing: 2-3 hours
- **Total remaining: ~4 hours**

---

## 🆘 Need Help?

- **Quick overview**: See `README.md` (3 commands to start!)
- **Complete guide**: See `INSTRUCTIONS.md`
- **Final setup**: See `FINAL_SETUP.md`
- **Problem specs**: Check `llm-codegen/data/*.json`
- **Test cases**: Check `llm-codegen/tests/test_*.py`

---

## ✅ Checklist

- [x] Install google-generativeai: `pip install google-generativeai`
- [x] Get Gemini API key from https://aistudio.google.com/app/apikey
- [x] Run `generate_with_gemini.py` (20 files) - DONE!
- [ ] Get Mistral API key from https://console.mistral.ai/
- [ ] Install mistralai: `pip install mistralai`
- [ ] Run `generate_with_mistral.py` (20 files)
- [ ] Run evaluation
- [ ] Debug 2+ failures (4+ files)
- [ ] Create innovation prompt
- [ ] Generate 20 innovation files
- [ ] Re-run evaluation
- [ ] Write report in METHODS_AND_RESULTS.md
- [ ] Export to Exercise1.pdf
- [ ] Push to GitHub
- [ ] Submit to Gradescope

---

## 🎯 Current Status

**You're 50% done with generation!**

✅ Gemini: 20 files created  
⏳ Mistral: Ready to generate (one command!)  
⏳ Evaluation: Ready to run  
⏳ Debugging & Innovation: After evaluation  

---

**Next step: Run Mistral generation!**

```cmd
set MISTRAL_API_KEY=your_key_here
pip install mistralai
python generate_with_mistral.py
```

Then evaluate:
```cmd
python llm-codegen\eval\run_eval.py
```

Good luck! 🚀
