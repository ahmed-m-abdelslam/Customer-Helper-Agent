import os
import litellm # type: ignore
import agentops  # type: ignore
from helpers.config import get_settings
from crewai import Agent , Task , Crew , Process , LLM  # type: ignore
from agents import SearchQueryRecommend , SearchEngine , Scraping , ProcurementReport
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource # type: ignore






# agentops.init(
#     api_key=get_settings().AGENTOPS_API_KEY,
# )

os.environ["OPENAI_API_KEY"] = get_settings().OPENAI_API_KEY

about_company = "ProHelper is a company that provides AI solutions to help websites refine their search and recommendation systems."

company_context = StringKnowledgeSource(
    content=about_company
)

search_agent = SearchQueryRecommend()
search_engine = SearchEngine()
scraping_agent = Scraping()
procurement_report_agent = ProcurementReport()


agent1, task1 = search_agent.get_agent()
agent2, task2 = search_engine.get_agent()
agent3, task3 = scraping_agent.get_agent()
agent4, task4 = procurement_report_agent.get_agent()


productname="coffee machine for the office"
countryname="Egypt"
nokeywords=5
language="English"
top_recommendations_no=10



#litellm._turn_on_debug()

crew = Crew(
            agents=[agent1,
                    agent2,
                    agent3,
                    agent4,
                ], 
            tasks=[task1,
                   task2,
                   task3,
                   task4,
            ],
            process = Process.sequential,
            knowledge_sources=[company_context],
            )
        
crew_results = crew.kickoff(
                 inputs={
                    "product_name": productname,
                    "country_name": countryname,
                    "no_keywords": nokeywords,
                    "language": language,
                    "top_recommendations_no": top_recommendations_no

            }
        )

