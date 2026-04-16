from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models.lite_llm import LiteLlm

try:
    from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH
except ImportError:
    from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH

morpheus_agent = RemoteA2aAgent(
    name="morpheus_agent",
    description="General-purpose assistant for broad user questions.",
    agent_card=f"http://127.0.0.1:8001{AGENT_CARD_WELL_KNOWN_PATH}",
)

neo_agent = RemoteA2aAgent(
    name="neo_agent",
    description="Neo specialist for requests that should be handled by Neo.",
    agent_card=f"http://127.0.0.1:9990{AGENT_CARD_WELL_KNOWN_PATH}",
)

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/gemma3:latest"),
    name="zion_agent",
    description="Unified front door for Morpheus and Neo.",
    instruction=(
        "You are the operator, the front door for multiple remote agents. "
        "Delegate broad assistant requests to morpheus_agent if directed at Morpheus. "
        "Delegate Neo-specific requests to neo_agent if directed at Neo. "
        "If one specialist is clearly the best fit, transfer to it."
        "If request cannot be routed, then reply not able to process with available agents"
    ),
    sub_agents=[morpheus_agent, neo_agent],
)
