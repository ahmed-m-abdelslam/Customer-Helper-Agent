from crewai import Agent , Task , Crew , Process  # type: ignore
from .BaseAgent import BaseAgent 
from helpers.config import get_settings
from AgentTools.AgentTools import AgentTools
from Schema.Schema import AllSearchResults


class SearchEngine(BaseAgent):
    def __init__(self):
        super().__init__()

        self.settings = get_settings()

    
    def get_agent(self) -> Agent:
        llm = self.llm( llm_name=self.settings.OPENAI_MODEL,
                        api_key=self.settings.OPENAI_API_KEY,)

        agent = Agent(
            name="SearchEngineAgent",
            role="Search Engine Agent",
            goal="To search for products based on the suggested search query",
            backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
            llm=llm,
            verbose=True,
            tools = [AgentTools.tavily_search_tool],
            
        )



        task = Task(
            name="SearchEngineAgent",
            description="\n".join([
    
                    "The task is to search for products based on the suggested search queries.",
                    "You have to collect results from multiple search queries.",
                    "Ignore any susbicious links or not an ecommerce single product website link.",
                    "Ignore any search results with confidence score less than (0.5) .",
                    "The search results will be used to compare prices of products from different websites.",
                
            ]),
            
            expected_output="A JSON object containing the search results.",
            output_json = AllSearchResults,
            output_file = str(self.data_path() / "step_2_search_results.json"),
            agent=agent
            
        )
        
        
        return agent , task