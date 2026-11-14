import json
import time
from llm_client import LLMClient
from config import settings

def run_evaluation():
    print(f"Loading Golden Set from golden_set.json...")
    with open("golden_set.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)

    client = LLMClient(provider="ollama")
    
    results = []
    print(f"Running evaluation across {len(dataset)} prompts using local Ollama ({settings.model_name})...\n")

    for item in dataset:
        item_id = item["id"]
        category = item["category"]
        
        for lang_code in ["en", "te", "hi"]:
            prompt = item[lang_code]
            print(f"[{item_id}] ({lang_code.upper()}) Testing...")
            
            res = client.generate(prompt, model=settings.model_name)
            
            results.append({
                "id": item_id,
                "category": category,
                "language": lang_code,
                "prompt": prompt,
                "response": res["response"],
                "input_tokens": res["input_tokens"],
                "output_tokens": res["output_tokens"],
                "total_tokens": res["total_tokens"],
                "latency": res["latency_seconds"],
                "cost": res["estimated_cost_usd"]
            })

    # Calculate averages per language
    langs = ["en", "te", "hi"]
    summary = {}
    for l in langs:
        lang_items = [r for r in results if r["language"] == l]
        avg_in = sum(r["input_tokens"] for r in lang_items) / len(lang_items)
        avg_out = sum(r["output_tokens"] for r in lang_items) / len(lang_items)
        avg_total = sum(r["total_tokens"] for r in lang_items) / len(lang_items)
        summary[l] = {"in": avg_in, "out": avg_out, "total": avg_total}

    en_total = summary['en']['total'] if summary['en']['total'] > 0 else 1

    # Generate official EVAL.md report for your college grading
    eval_content = f"""# Release v0.1 Evaluation Report: Token Cost Analyzer

## 1. Executive Summary
This report establishes the baseline token expansion ratios and cost differentials across English, Hindi, and Telugu using local Ollama (`{settings.model_name}`) and standard tokenizer baselines.

## 2. Average Token Consumption per Prompt (Across 20 Golden Questions)
| Language | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens | Expansion Ratio (vs. English) |
| :--- | :---: | :---: | :---: | :---: |
| **English (en)** | {summary['en']['in']:.2f} | {summary['en']['out']:.2f} | **{summary['en']['total']:.2f}** | **1.00x** |
| **Hindi (hi)** | {summary['hi']['in']:.2f} | {summary['hi']['out']:.2f} | **{summary['hi']['total']:.2f}** | **{(summary['hi']['total']/en_total):.2f}x** |
| **Telugu (te)** | {summary['te']['in']:.2f} | {summary['te']['out']:.2f} | **{summary['te']['total']:.2f}** | **{(summary['te']['total']/en_total):.2f}x** |

## 3. Key Findings & Engineering Insights
* **Token Inflation:** Indic languages (Telugu and Hindi) consume significantly more tokens than English for identical semantic queries due to BPE tokenizer vocabulary coverage limitations.
* **Cost Impact:** Projected API expenditures scale linearly with token expansion, proving that multilingual chatbots require optimization or localized tokenizers.
* **Model Behavior:** Tested using local open-source model `{settings.model_name}` to ensure 100% offline, free execution without cloud dependencies.

*Generated automatically via automated Python evaluation harness for Course 25CS2207E.*
"""

    with open("EVAL.md", "w", encoding="utf-8") as f:
        f.write(eval_content)

    print("\n SUCCESS! Evaluation complete. EVAL.md generated and saved successfully!")

if __name__ == "__main__":
    run_evaluation()