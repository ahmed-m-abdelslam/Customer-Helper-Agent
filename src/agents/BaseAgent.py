from crewai import  LLM  # type: ignore
from pydantic import BaseModel , Field # type: ignore
import os , sys
from pathlib import Path

class BaseAgent:
    def __init__(self):
        pass

    @staticmethod
    def llm(llm_name: str ,
            temperature: float = 0 ,
            base_url: str = None ,
            api_key: str = None,
            max_tokens : int = 1000
            ) -> LLM:

        llm = LLM(model = llm_name,
                   temperature = temperature, 
                   base_url = base_url, 
                   api_key = api_key, 
                   max_tokens = max_tokens
                   )

        return llm
    
    def data_path(self) -> Path:
        
        base_dir = Path(__file__).resolve().parents[1]  # src
        data_dir = base_dir / "DataFiles"
        
        data_dir.mkdir(parents=True, exist_ok=True)

        if not data_dir.exists():
            raise FileNotFoundError(f"Data folder not found: {data_dir}")

        return data_dir

    
class SuggestionSearchQueries(BaseModel):
    search_queries: list[str] = Field(..., description="A list of suggested search queries",
                                      min_items=1, max_items=10)