from crewai import Agent , Task , Crew , Process , LLM  # type: ignore
import agentops  # type: ignore
from helpers.config import get_settings
from agents.SearchQueryRecommend import SearchQueryRecommend

search_agent = SearchQueryRecommend(
    productname="coffee machine for the office", 
    websiteslist=["amazon.com", "noon.com", "jumia.com"],
    countryname="Egypt",
    nokeywords=10,
    language="English"
)

print(search_agent.get_agent())