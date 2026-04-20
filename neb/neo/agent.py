from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.a2a.utils.agent_to_a2a import to_a2a

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/gemma4:latest"),
    name="neo_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge.",
)

app = to_a2a(root_agent, port=9990)
