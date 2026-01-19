from crewai import Agent , Task , Crew , Process , LLM  # type: ignore
import agentops  # type: ignore
class Crewops:
    def __init__(self, agentops_key: str):
        self.agentops_key = agentops_key

    def initialize_agentops(self):
        agentops.init(
            api_key=self.agentops_key,
            skip_auto_end_session=False,
        )
        