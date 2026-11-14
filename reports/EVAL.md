# Release v0.1 Evaluation Report: Token Cost Analyzer

## 1. Executive Summary
This report establishes the baseline token expansion ratios and cost differentials across English, Hindi, and Telugu using local Ollama (`llama3.2:1b`) and standard tokenizer baselines.

## 2. Average Token Consumption per Prompt (Across 20 Golden Questions)
| Language | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens | Expansion Ratio (vs. English) |
| :--- | :---: | :---: | :---: | :---: |
| **English (en)** | 9.30 | 305.25 | **314.55** | **1.00x** |
| **Hindi (hi)** | 46.75 | 923.85 | **970.60** | **3.09x** |
| **Telugu (te)** | 81.85 | 844.40 | **926.25** | **2.94x** |

## 3. Key Findings & Engineering Insights
* **Token Inflation:** Indic languages (Telugu and Hindi) consume significantly more tokens than English for identical semantic queries due to BPE tokenizer vocabulary coverage limitations.
* **Cost Impact:** Projected API expenditures scale linearly with token expansion, proving that multilingual chatbots require optimization or localized tokenizers.
* **Model Behavior:** Tested using local open-source model `llama3.2:1b` to ensure 100% offline, free execution without cloud dependencies.

*Generated automatically via automated Python evaluation harness for Course 25CS2207E.*
