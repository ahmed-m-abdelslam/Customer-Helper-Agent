from crewai import Agent , Task , Crew , Process  # type: ignore
from .BaseAgent import BaseAgent, SuggestionSearchQueries
from helpers.config import get_settings


class SearchQueryRecommend(BaseAgent):
    def __init__(self, productname: str, 
                 websiteslist: list[str], 
                 countryname: str , 
                 nokeywords: int, 
                 language: str):
        super().__init__()
        self.productname = productname
        self.websiteslist = websiteslist
        self.countryname = countryname
        self.nokeywords = nokeywords
        self.language = language
        self.settings = get_settings()

    
    def get_agent(self) -> Agent:
        llm = self.llm( llm_name=self.settings.GROQ_MODEL_ID,
                        api_key=self.settings.GROQ_API_KEY,)

        agent = Agent(
            name="SearchQueryRecommendAgent",
            role="An agent that recommends optimized search queries based on user input.",
            goal = "\n".join([
                "To suggest effective search queries that enhance search results for users.",
                "The queries should be relevant, specific, and likely to yield high-quality results."
                ]),
            backstory="Experienced in understanding user intent and optimizing search queries.",
            llm=llm,
            verbose=True
        )



        task = Task(
            name="SearchQueryRecommendAgent",
            description="\n".join([
                "Rankyx is looking to buy {product_name} at the best prices (value for a price strategy)",
                "The campany target any of these websites to buy from: {websites_list}",
                "The company wants to reach all available proucts on the internet to be compared later in another stage.",
                "The stores must sell the product in {country_name}",
                "Generate at maximum {no_keywords} queries.",
                "The search keywords must be in {language} language.",
                "Search keywords must contains specific brands, types or technologies. Avoid general keywords.",
                "The search query must reach an ecommerce webpage for product, and not a blog or listing page."
            ]),
            expected_output="A JSON object containing a list of suggested search queries.",
            output_json = SuggestionSearchQueries,

            output_file = str(self.data_path() / "step_1_search_query_recommendations.json"),
            agent=agent
            
        )
        
        crew = Crew(
            agents=[agent], 
            tasks=[task],
            process = Process.sequential
            )
        
        crew_results = crew.kickoff(
                 inputs={
                    "product_name": self.productname,
                    "websites_list": ", ".join(self.websiteslist),
                    "country_name": self.countryname,
                    "no_keywords": self.nokeywords,
                    "language": self.language
            }
        )

       
        
        return crew_results