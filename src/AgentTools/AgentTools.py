from helpers.config import get_settings
from tavily import TavilyClient  # type: ignore
from crewai.tools import tool  # type: ignore
from scrapegraph_py import Client  # type: ignore
import json


class AgentTools:
    def __init__(self):
        pass

    @staticmethod
    @tool("tavily_search")
    def tavily_search_tool(query: str):
        """
        Useful for search-based queries. Use this to find current information about any query related pages using a search engine
        
        """
        search_client = TavilyClient(api_key=get_settings().TAVILY_API_KEY,)

        return search_client.search(query)


    @staticmethod
    @tool("scrapegraph_search")
    def web_scrape_tool(page_url: str, required_fields: list):
        """
            An AI Tool to help an agent to scrape a web page
            Example:
            web_scraping_tool(
                page_url="https://www.noon.com/egypt-en/15-bar-fully-automatic-espresso-machine-1-8-l-1500"
            )
        
        """
        scrape_client = Client(api_key=get_settings().SCRAPE_API_KEY,)
        details = scrape_client.smartscraper(
            wepsite_url=page_url,
            user_prompt="Extract" + json.dumps(required_fields , ensure_ascii=False) + "from the web page",
        )

        return {
            "page_url": page_url,
            "details": details,
        }