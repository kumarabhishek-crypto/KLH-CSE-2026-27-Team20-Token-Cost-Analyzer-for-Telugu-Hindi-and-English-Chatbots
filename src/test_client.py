from llm_client import LLMClient
from config import settings

client = LLMClient(provider="ollama")

prompts = {
    "English": "What is the capital of India? Answer in one short sentence.",
    "Telugu": "భారతదేశ రాజధాని ఏది? ఒక చిన్న వాక్యంలో సమాధానం చెప్పండి.",
    "Hindi": "भारत की राजधानी क्या है? एक छोटे वाक्य में उत्तर दें।"
}

print(f"Running multilingual test on local Ollama ({settings.model_name})...\n")

for lang, prompt in prompts.items():
    result = client.generate(prompt, model=settings.model_name)
    print(f"=== {lang} ===")
    print(f"Prompt: {prompt}")
    print(f"Response: {result['response']}")
    print(f"Input Tokens: {result['input_tokens']} | Output Tokens: {result['output_tokens']} | Total: {result['total_tokens']}")
    print(f"Latency: {result['latency_seconds']}s | Est. API Cost (GPT-4o-mini eq.): ${result['estimated_cost_usd']}\n")