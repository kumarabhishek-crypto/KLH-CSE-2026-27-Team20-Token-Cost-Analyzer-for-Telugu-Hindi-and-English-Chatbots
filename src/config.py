from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "not-needed-using-ollama"
    ollama_base_url: str = "http://localhost:11434"
    model_name: str = "llama3.2:1b"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()