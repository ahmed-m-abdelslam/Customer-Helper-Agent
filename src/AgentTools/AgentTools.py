from helpers.config import get_settings
from tavily import TavilyClient  # type: ignore
from crewai.tools import tool  # type: ignore


class AgentTools:
    def __init__(self):
        pass

    @staticmethod
    @tool("tavily_search")
    def tavily_search_tool(query: str):
        """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
        search_client = TavilyClient(api_key=get_settings().TAVILY_API_KEY,)

        return search_client.search(query)
