from pydantic_settings import BaseSettings , SettingsConfigDict # type: ignore

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    AGENTOPS_API_KEY: str
   

    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()