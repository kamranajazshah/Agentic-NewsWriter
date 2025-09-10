from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools import tool
load_dotenv()
chatllm=ChatOpenAI()
researchagent=Agent(
    role="Senior Researcher",
    goal="Unccover ground breaking technologies in {topic}",
    llm=chatllm,
    verbose=True,
    allow_delegation=True,
    backstory=(  "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."),
    tools=[tool]
    
)
newsWriter=Agent(
    role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=chatllm,
  allow_delegation=False

)