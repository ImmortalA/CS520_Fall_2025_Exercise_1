# CS520 Exercise 1: LLM Code Generation Evaluation

This repository contains the implementation and evaluation of different prompting strategies for Large Language Model (LLM) code generation using the HumanEval+ dataset.

## 📊 Key Results Summary

| Strategy | Gemini | Mistral | Overall |
|----------|--------|---------|---------|
| **Chain-of-Thought (CoT)** | 90.0% | 70.0% | 80.0% |
| **Stepwise Chain-of-Thought (SCoT)** | 100.0% | 70.0% | 85.0% |
| **Test-Driven Refinement (Innovation)** | 70.0% | 30.0% | 50.0% |

### Key Findings:
- **SCoT outperformed CoT** on Gemini (100% vs 90%) but tied on Mistral (70% vs 70%)
- **Self-repair strategy** successfully fixed 3/3 selected failure cases
- **Innovation strategy failed** with 50% overall performance vs 85% baseline
- **Gemini consistently outperformed Mistral** across all strategies

## 📁 Repository Structure

```
├── Exercise1_Report.tex          # Complete LaTeX report (874 lines)
├── Exercise1.pdf                 # Compiled PDF report
├── generate_with_gemini.py       # Gemini API generation script
├── generate_with_mistral.py     # Mistral API generation script
├── generate_self_repair.py      # Self-repair generation script
├── generate_innovation.py       # Innovation strategy generation script
└── llm-codegen/
    ├── data/                     # 10 HumanEval+ problem specifications
    ├── prompts/                  # 4 prompt templates (CoT, SCoT, self-repair, innovation)
    ├── generations/              # 60+ generated code solutions
    ├── tests/                    # Test cases for all problems
    └── eval/                     # Evaluation scripts and results
        ├── results.csv           # Part 1 baseline results
        ├── results_part2.csv     # Part 2 self-repair results  
        ├── results_part3.csv     # Part 3 innovation results
        └── run_eval*.py          # Evaluation scripts
```

## 🎯 Project Overview

**Objective**: Evaluate prompting strategies for LLM code generation

**Dataset**: 10 diverse problems from HumanEval+ dataset

**LLM Families**: 
- Google DeepMind (Gemini)
- Mistral AI (Mistral)

**Strategies Evaluated**:
1. **Chain-of-Thought (CoT)**: Basic reasoning approach
2. **Stepwise Chain-of-Thought (SCoT)**: Structured reasoning approach  
3. **Self-Repair**: Debugging failed solutions with targeted feedback
4. **Test-Driven Refinement**: Novel strategy focusing on explicit edge case enumeration

## 📈 Detailed Results

### Part 1: Baseline Evaluation
- **Total Solutions Generated**: 40 (10 problems × 2 families × 2 strategies)
- **Gemini SCoT**: Perfect performance (100% pass@1)
- **Mistral**: Consistent 70% performance across CoT and SCoT

### Part 2: Debugging Analysis
- **Failures Identified**: 7 total failures across families
- **Self-Repair Cases**: 3 representative failures selected
- **Success Rate**: 100% (3/3 failures fixed)
- **Key Insight**: Targeted debugging feedback with specific test cases enables LLMs to generate correct solutions

### Part 3: Innovation Strategy
- **Novel Approach**: Test-Driven Refinement with explicit edge case enumeration
- **Performance**: 50% overall vs 85% baseline (-35% decline)
- **Key Finding**: Explicit edge case enumeration hindered rather than helped model performance
- **Family Impact**: Gemini more resilient (70%) than Mistral (30%)

## 📋 Deliverables Checklist

✅ **PDF Report**: Complete analysis with methodology, results, and discussion  
✅ **Prompts**: All prompt templates included in `llm-codegen/prompts/`  
✅ **Generated Code**: 60+ solutions organized by problem/family/strategy  
✅ **Test Cases**: HumanEval+ test cases for all problems  
✅ **Evaluation Scripts**: Complete evaluation harness and results  
✅ **GitHub Repository**: Clean, professional repository structure

## 🔬 Methodology

1. **Problem Selection**: 10 diverse HumanEval+ problems spanning different difficulty levels
2. **Generation**: API calls to Gemini and Mistral using different prompting strategies
3. **Evaluation**: Automated testing using HumanEval+ test cases with pass@1 metrics
4. **Analysis**: Statistical comparison across strategies and families

## 📊 Problem-by-Problem Results

| Problem | Gemini CoT | Gemini SCoT | Gemini Innovation | Mistral CoT | Mistral SCoT | Mistral Innovation |
|---------|------------|-------------|-------------------|-------------|--------------|-------------------|
| humaneval_0 | 100% | 100% | 0% | 100% | 100% | 0% |
| humaneval_1 | 100% | 100% | 0% | 100% | 100% | 0% |
| humaneval_10 | 100% | 100% | 100% | 100% | 100% | 100% |
| humaneval_108 | 0% | 100% | 100% | 0% | 0% | 0% |
| humaneval_12 | 100% | 100% | 100% | 100% | 100% | 0% |
| humaneval_17 | 100% | 100% | 100% | 100% | 100% | 0% |
| humaneval_25 | 100% | 100% | 0% | 0% | 0% | 0% |
| humaneval_31 | 100% | 100% | 100% | 100% | 100% | 100% |
| humaneval_54 | 100% | 100% | 100% | 0% | 0% | 0% |
| humaneval_61 | 100% | 100% | 100% | 100% | 100% | 100% |

## 🎓 Academic Contribution

This work provides empirical evidence on:
- **Prompting strategy effectiveness** across different LLM families
- **Self-repair capabilities** of modern LLMs for code debugging
- **Limitations of complex prompting** approaches
- **Family-specific performance patterns** in code generation

## 📖 Report

The complete analysis is documented in `Exercise1_Report.tex` (874 lines) and compiled as `Exercise1.pdf`, including:
- Detailed methodology and experimental setup
- Comprehensive results with pass@k metrics
- Debugging analysis with self-repair examples
- Innovation strategy discussion and failure analysis
- Statistical significance testing and family comparisons

## 🚀 Usage

To reproduce results:
1. Set API keys: `GEMINI_API_KEY` and `MISTRAL_API_KEY`
2. Run generation scripts: `python generate_with_*.py`
3. Execute evaluation: `python llm-codegen/eval/run_eval.py`
4. Compile report: `pdflatex Exercise1_Report.tex`

## 📝 Files Included

### Prompts and Workflows
- `llm-codegen/prompts/cot_generic.txt` - Chain-of-Thought template
- `llm-codegen/prompts/scot_generic.txt` - Stepwise Chain-of-Thought template
- `llm-codegen/prompts/self_repair_generic.txt` - Self-repair template
- `llm-codegen/prompts/test_driven_refinement.txt` - Innovation template

### Generated Code
- `llm-codegen/generations/` - Complete set of 60+ generated solutions
- Organized by problem → family → strategy hierarchy

### Test Cases
- `llm-codegen/tests/` - HumanEval+ test cases for all 10 problems
- `llm-codegen/data/` - Problem specifications and constraints

### Evaluation Scripts and Results
- `llm-codegen/eval/run_eval.py` - Main evaluation harness
- `llm-codegen/eval/results*.csv` - Complete evaluation results
- `llm-codegen/eval/compare_*.py` - Strategy comparison scripts