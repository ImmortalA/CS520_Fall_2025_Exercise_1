# Exercise 1: Code Generation with Gemini + Mistral

Complete setup for evaluating code generation across two LLM families.

## Quick Start (3 Commands)

### 1. Generate with Gemini API
```cmd
set GEMINI_API_KEY=your_gemini_key
python generate_with_gemini.py
```
**Output**: 20 files in `gemini/` folders

### 2. Generate with Mistral AI API
```cmd
set MISTRAL_API_KEY=your_mistral_key
pip install mistralai
python generate_with_mistral.py
```
**Output**: 20 files in `mistral/` folders

### 3. Run Evaluation
```cmd
python llm-codegen\eval\run_eval.py
type llm-codegen\eval\results.csv
```
**Output**: Pass@1 and pass@3 metrics

---

## Setup Details

### Get API Keys

**Gemini**: https://aistudio.google.com/app/apikey (Free)
**Mistral**: https://console.mistral.ai/ (Free tier available)

### Set Environment Variables
```cmd
set GEMINI_API_KEY=your_gemini_api_key_here
set MISTRAL_API_KEY=your_mistral_api_key_here
```

### Install Dependencies
```cmd
pip install google-generativeai mistralai
```

---

## Repository Structure

```
llm-codegen/
  data/              - 10 HumanEval+ problems (JSON specs)
  tests/             - 10 comprehensive test files
  prompts/           - CoT, SCoT, Self-Repair templates
  generations/       - Generated solutions (40+ files)
    humaneval_X/
      gemini/
        cot/         - Chain-of-Thought
        scot/        - Stepwise CoT
      mistral/
        cot/
        scot/
  eval/
    run_eval.py      - Evaluation script
    results.csv      - Pass@k metrics
```

---

## LLM Families

1. **Gemini 2.5 Flash** (Google DeepMind)
   - Model: `models/gemini-2.5-flash`
   - Access: Google AI Studio API

2. **Mistral Large** (Mistral AI)
   - Model: `mistral-large-latest`
   - Access: Mistral La Plateforme API

Both are distinct model families as required.

---

## Problems (HumanEval+)

1. humaneval_0 - has_close_elements
2. humaneval_1 - separate_paren_groups
3. humaneval_10 - make_palindrome
4. humaneval_12 - longest
5. humaneval_17 - parse_music
6. humaneval_25 - factorize
7. humaneval_31 - is_prime
8. humaneval_54 - same_chars
9. humaneval_61 - correct_bracketing
10. humaneval_108 - count_nums

---

## After Generation

### Run Evaluation
```cmd
python llm-codegen\eval\run_eval.py
```

### Check Results
```cmd
type llm-codegen\eval\results.csv
```

Results show:
- problem_id
- family (gemini/mistral)
- strategy (cot/scot)
- n_samples, n_correct
- pass@1, pass@3

---

## Next Steps

1. **Debug Failures** (Part 2)
   - Find 2+ problems with `pass@1 = 0.000`
   - Use `self_repair` strategy
   - Document before/after

2. **Innovation** (Part 3)
   - Create novel prompting strategy
   - Test on both families
   - Compare results

3. **Report** 
   - Fill `llm-codegen/report/METHODS_AND_RESULTS.md`
   - Export to `Exercise1.pdf`
   - Include GitHub link

4. **Submit**
   - Upload PDF to Gradescope
   - Deadline: Oct 22, 11:59 PM EST

---

## File Count

- Data: 10 problems
- Tests: 10 test files
- Prompts: 3 templates
- Generations: 40+ files minimum
  - 20 Gemini (10×2 strategies)
  - 20 Mistral (10×2 strategies)
  - 4+ Self-repair (debugging)
  - 20+ Innovation strategy

---

## Troubleshooting

**Gemini API 404 error?**
- Run with correct model: `models/gemini-2.5-flash`
- Check API key is valid

**Mistral API error?**
- Ensure `mistralai` library installed: `pip install mistralai`
- Verify API key from https://console.mistral.ai/
- Check you have API access (free tier available)

**Evaluation fails?**
- Ensure function names match problem specs
- Check files are in correct folder structure
- No top-level code except function definitions

---

## Documentation

- **README.md** (this file) - Quick start
- **QUICK_START.md** - Detailed guide
- **INSTRUCTIONS.md** - Complete walkthrough
- **START_HERE.txt** - Overview

---

## Time Estimate

- Gemini generation: 3-5 minutes (API)
- Mistral generation: 3-5 minutes (API)
- First evaluation: 1 minute
- Self-repair: 30 minutes
- Innovation: 1 hour
- Report: 2-3 hours

**Total: ~4-5 hours**

---

## Ready!

Everything is set up. Just run the two generation scripts and evaluate!

```cmd
python generate_with_gemini.py
python generate_with_mistral.py
python llm-codegen\eval\run_eval.py
```

Good luck! 🚀

