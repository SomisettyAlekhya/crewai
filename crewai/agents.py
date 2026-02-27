# agents.py
from crewai import Agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found! Please set it in .env file.")

# Initialize OpenAI LLM
llm = OpenAI(openai_api_key=api_key, temperature=0)

# Define CrewAI agents
reader = Agent(
    role="PDF Reader",
    goal="Extract key study points from uploaded PDF",
    backstory="Expert at reading documents and identifying important concepts.",
    verbose=True,
    llm=llm
)

teacher = Agent(
    role="Concept Teacher",
    goal="Explain extracted concepts simply",
    backstory="Transforms complex content into easy learning notes.",
    verbose=True,
    llm=llm
)

quiz_master = Agent(
    role="Quiz Generator",
    goal="Create quiz questions with one-line answers",
    backstory="Creates short revision quizzes for students.",
    verbose=True,
    llm=llm
)