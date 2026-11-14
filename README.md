# KLH-CSE-2026-27-Team20-Token-Cost-Analyzer-for-Telugu-Hindi-and-English-Chatbots

## Project Metadata
* **Project Title:** Token Cost Analyzer for Telugu, Hindi and English Chatbots
* **Course Code:** 25CS2207E (Generative AI and AI Platform Engineering)
* **Team ID:** Team 20
* **Team Members:** 
  * RAKESH MEDIKONDA 2520030035
  * JASHWANTH 2520030597
  * ABHISHEK KUMAR 2520030448
* **Supervisor / Coordinator:** Dr. V. Anu Ragavi
* **Current Project Phase Status:** Phase 1 Completed (Baseline Tokenization & Evaluation locked under `review-1`)

## Abstract
Multilingual LLM applications deployed for Indic languages (such as Telugu and Hindi) frequently suffer from severe token inflation due to subword tokenization bias in English-centric vocabulary spaces. This project measures, benchmarks, and analyzes token expansion ratios, latency, and projected cost differentials across English, Hindi, and Telugu using local execution models (Ollama `llama3.2:1b`) and standard tokenizer baselines.

## Repository Structure
```text
├── src/          # Core source code (LLM client, configuration, eval runner)
├── data/         # Datasets and Golden Sets (golden_set.json)
├── reports/      # Evaluation reports and benchmark summaries (EVAL.md)
├── docs/         # Project documentation and architectural notes
└── results/      # Execution logs and raw evaluation outputs