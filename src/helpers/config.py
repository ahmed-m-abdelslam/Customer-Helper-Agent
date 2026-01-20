from pydantic_settings import BaseSettings , SettingsConfigDict # type: ignore

class Settings(BaseSettings):
    
    AGENTOPS_API_KEY: str

    OLLAMA_MODELL_ONE: str
    OLLAMA_MODELL_TWO: str
    BASE_URL: str
    
    GROQ_API_KEY: str
    GROQ_MODEL_ID: str

    TAVILY_API_KEY: str

    OPENAI_API_KEY: str
    OPENAI_MODEL: str

    SCRAPE_API_KEY: str
   

    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()