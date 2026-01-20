from crewai import Agent , Task , Crew , Process , LLM  # type: ignore
import agentops  # type: ignore
from helpers.config import get_settings
from agents import SearchQueryRecommend , SearchEngine
import litellm # type: ignore
import os




# agentops.init(
#     api_key=get_settings().AGENTOPS_API_KEY,
# )

os.environ["OPENAI_API_KEY"] = get_settings().OPENAI_API_KEY

search_agent = SearchQueryRecommend()
search_engine = SearchEngine()

agent1, task1 = search_agent.get_agent()
agent2, task2 = search_engine.get_agent()





productname="coffee machine for the office"
countryname="Egypt"
nokeywords=5
language="English"


#litellm._turn_on_debug()

crew = Crew(
            agents=[agent1,
                    agent2,
                ], 
            tasks=[task1,
                   task2,
            ],
            process = Process.sequential
            )
        
crew_results = crew.kickoff(
                 inputs={
                    "product_name": productname,
                    "country_name": countryname,
                    "no_keywords": nokeywords,
                    "language": language,
            }
        )

