# ✅ FINAL SETUP: Gemini + Mistral (Ready to Run!)

## What's Changed

✅ **Removed**: All ChatGPT references
✅ **Added**: Automated Mistral AI API script
✅ **Updated**: All documentation for Gemini + Mistral workflow

---

## 🚀 Your Complete Workflow (3 Commands)

### Prerequisites

Get API keys:
- **Gemini**: https://aistudio.google.com/app/apikey (Free)
- **Mistral**: https://console.mistral.ai/ (Free tier available)

---

### Command 1: Generate with Gemini
```cmd
cd /d D:\Umass\Semester_3\cs520\exercise_1
set GEMINI_API_KEY=your_gemini_key_here
python generate_with_gemini.py
```
**Time**: 3-5 minutes  
**Output**: 20 files in `gemini/` folders

---

### Command 2: Generate with Mistral
```cmd
set MISTRAL_API_KEY=your_mistral_key_here
pip install mistralai
python generate_with_mistral.py
```
**Time**: 3-5 minutes  
**Output**: 20 files in `mistral/` folders

---

### Command 3: Run Evaluation
```cmd
python llm-codegen\eval\run_eval.py
type llm-codegen\eval\results.csv
```
**Time**: 1 minute  
**Output**: Pass@k metrics for both families

---

## 📁 What You'll Have

```
llm-codegen/generations/
  humaneval_0/
    gemini/
      cot/cot_sample1.py
      scot/scot_sample1.py
    mistral/
      cot/cot_sample1.py
      scot/scot_sample1.py
  humaneval_1/
    ... (same structure)
  ... (all 10 problems)

Total: 40 files minimum
```

---

## 🎯 LLM Families (Assignment Requirement)

1. **Gemini 2.5 Flash** - Google DeepMind family
2. **Mistral Large** - Mistral AI family

✅ Both are distinct families  
✅ Satisfies "at least two LLMs from different families"  
✅ Both use API (consistent, automated workflow)

---

## 📊 Expected Results

`llm-codegen/eval/results.csv` will show:

| problem_id | family | strategy | n_samples | n_correct | pass@1 | pass@3 |
|------------|--------|----------|-----------|-----------|--------|--------|
| humaneval_0 | gemini | cot | 1 | ? | ? | ? |
| humaneval_0 | gemini | scot | 1 | ? | ? | ? |
| humaneval_0 | mistral | cot | 1 | ? | ? | ? |
| humaneval_0 | mistral | scot | 1 | ? | ? | ? |
| ... | ... | ... | ... | ... | ... | ... |

---

## 📝 After Evaluation

### Part 2: Debugging (30 minutes)

1. Find 2+ problems where `pass@1 = 0.000`
2. For each failure:
   - Check the test file
   - Use `self_repair` prompting
   - Generate fixed version
   - Save to `<family>/self_repair/self_repair_sample1.py`
3. Re-run evaluation

### Part 3: Innovation (1 hour)

1. Create new prompt: `llm-codegen/prompts/your_strategy.txt`
2. Generate for both families (20 files)
3. Evaluate and compare pass@k

### Part 4: Report (2-3 hours)

Fill `llm-codegen/report/METHODS_AND_RESULTS.md`:
- LLM families used
- Problems selected
- Exact prompts
- Results tables
- Debugging analysis
- Innovation discussion
- GitHub link

Export to `Exercise1.pdf` and submit!

---

## 🛠️ Scripts Available

- **generate_with_gemini.py** - Auto-generate Gemini solutions
- **generate_with_mistral.py** - Auto-generate Mistral solutions  
- **llm-codegen/eval/run_eval.py** - Evaluate all solutions

---

## 📚 Documentation

- **README.md** - Quick 3-command start (read first!)
- **START_HERE.txt** - Overview
- **QUICK_START.md** - Detailed guide
- **INSTRUCTIONS.md** - Complete walkthrough
- **REPO_STATUS.md** - Verification checklist

---

## ⏰ Time Breakdown

| Task | Time |
|------|------|
| Gemini API generation | 5 min |
| Mistral API generation | 5 min |
| First evaluation | 1 min |
| Debugging 2+ failures | 30 min |
| Innovation strategy | 1 hour |
| Report writing | 2-3 hours |
| **TOTAL** | **4-5 hours** |

---

## ✅ Verification Checklist

Before starting:
- [ ] Have Gemini API key
- [ ] Have Mistral API key (free tier)
- [ ] `google-generativeai` installed
- [ ] `mistralai` library installed

After generation:
- [ ] 20 Gemini files created
- [ ] 20 Mistral files created
- [ ] Evaluation runs successfully
- [ ] `results.csv` contains 40+ rows

Before submission:
- [ ] 2+ failures debugged
- [ ] Innovation strategy tested
- [ ] Report complete
- [ ] PDF exported
- [ ] GitHub link included

---

## 🎓 Assignment Alignment

**Part 1** (40%): Gemini + Mistral × CoT + SCoT = 40 files ✓  
**Part 2** (30%): Debug 2+ failures with self-repair ✓  
**Part 3** (30%): Novel strategy tested on both families ✓  

---

## 🚦 Current Status

✅ Repository cleaned (no ChatGPT references)  
✅ Gemini script ready  
✅ Mistral script ready  
✅ Evaluation script ready  
✅ Documentation updated  
✅ All systems go!

---

## 🎯 Next Action

**Run these 3 commands:**

```cmd
python generate_with_gemini.py
python generate_with_mistral.py
python llm-codegen\eval\run_eval.py
```

Then check `llm-codegen\eval\results.csv` to see how both families performed!

---

**You're ready to complete the assignment! 🚀**

Deadline: Oct 22, 11:59 PM EST

