import streamlit as st
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.agents import Agent
from src.prompts import raspberry_agents


agent_1 = Agent(
    name="Agent1",
    prompt=raspberry_agents["Agent1"],
)

agent_2 = Agent(
    name="Agent2",
    prompt=raspberry_agents["Agent2"],
)

user_prompt = "Hi Agent, could you count the letters 'r' in the word raspberry?"

response_1 = agent_1.deploy_agent(user_prompt)
response_2 = agent_2.deploy_agent(f"What the user initially asked: {user_prompt}. What Agent 1 proposes: {response_1}")