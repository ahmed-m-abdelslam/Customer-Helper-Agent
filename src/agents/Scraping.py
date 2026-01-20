from crewai import Agent , Task , Crew , Process  # type: ignore
from .BaseAgent import BaseAgent ,AllSearchResults
from helpers.config import get_settings
from AgentTools.AgentTools import AgentTools


class Scraping(BaseAgent):
    def __init__(self):
        super().__init__()
        self.settings = get_settings()

    
    def get_agent(self) -> Agent:
        llm = self.llm( llm_name=self.settings.OPENAI_MODEL,
                        api_key=self.settings.OPENAI_API_KEY,)

        agent = Agent(
            name="ScrapingAgent",
            role="Scraping Agent",
            goal="To extract details from any website",
            backstory="The agent is designed to help in looking for required values from any website url. These details will be used to decide which best product to buy.",
            llm=llm,
            verbose=False,
            tools = [AgentTools.web_scrape_tool],
            
        )



        task = Task(
            name="ScrapingAgent",
            description="\n".join([
    
                "The task is to extract product details from any ecommerce store page url.",
                "The task has to collect results from multiple pages urls.",
                "Collect the best {top_recommendations_no} products from the search results.",     
                
            ]),
            
            expected_output="A JSON object containing the search results.",
            output_json = AllSearchResults,
            output_file = str(self.data_path() / "step_3_scraping_results.json"),
            agent=agent
            
        )
        
        
        return agent , task