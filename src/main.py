from crewai import Agent , Task , Crew , Process , LLM  # type: ignore
import agentops  # type: ignore
from helpers.config import get_settings
from agents.SearchQueryRecommend import SearchQueryRecommend


agentops.init(
    api_key=get_settings().AGENTOPS_API_KEY,
)
search_agent = SearchQueryRecommend(
    productname="coffee machine for the office", 
    websiteslist=["www.amazon.com", "www.noon.com", "www.jumia.com"],
    countryname="Egypt",
    nokeywords=10,
    language="English"
)

print(search_agent.get_agent())