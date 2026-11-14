import time
import tiktoken
from openai import OpenAI
from config import settings

class LLMClient:
    def __init__(self, provider: str = "openai"):
        self.provider = provider
        if provider == "openai":
            self.client = OpenAI(api_key=settings.openai_api_key)
        elif provider == "ollama":
            # Connects to local Ollama instance running on your PC
            self.client = OpenAI(
                base_url=f"{settings.ollama_base_url}/v1",
                api_key="ollama"  # Ollama doesn't require a real key
            )

    def count_tokens(self, text: str, model: str = "gpt-4o-mini") -> int:
        """Accurately measures token counts using tiktoken."""
        try:
            encoding = tiktoken.encoding_for_model(model)
        except Exception:
            encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))

    def generate(self, prompt: str, model: str = "gpt-4o-mini"):
        """Sends a prompt, tracks latency, computes tokens, and estimates cost."""
        start_time = time.time()
        
        input_tokens = self.count_tokens(prompt, model)
        
        if self.provider == "openai":
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            output_text = response.choices[0].message.content
            output_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
        else:
            # Ollama local generation
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            output_text = response.choices[0].message.content
            output_tokens = self.count_tokens(output_text, model)
            total_tokens = input_tokens + output_tokens

        end_time = time.time()
        latency = round(end_time - start_time, 2)

        # Cost estimation per 1M tokens (Standard GPT-4o-mini pricing baseline: $0.15/1M in, $0.60/1M out)
        estimated_cost = (input_tokens * 0.00015 / 1000) + (output_tokens * 0.0006 / 1000)

        log_data = {
            "prompt": prompt,
            "response": output_text,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "latency_seconds": latency,
            "estimated_cost_usd": round(estimated_cost, 6)
        }

        return log_data

if __name__ == "__main__":
    # Quick test runner
    client = LLMClient(provider="openai" if settings.openai_api_key != "your-api-key-here" else "ollama")
    print("LLM Client initialized successfully!")