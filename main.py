import streamlit as st
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.agents import Agent
from src.prompts import raspberry_agents
import json


agent_1 = Agent(
    name="Agent1",
    prompt=raspberry_agents["Agent1"],
)

agent_2 = Agent(
    name="Agent2",
    prompt=raspberry_agents["Agent2"],
)

agent_3 = Agent(
    name="Agent3",
    prompt=raspberry_agents["Agent3"],
)

headline = st.header("Chain of thought reasoning")
sidebar = st.sidebar
user_prompt = st.text_input("User prompt", "Hi Agent, could you count the letters 'r' in the word raspberry?")
button = st.button("Start reasoning")
response = st.container()

if button:
    response_1 = agent_1.deploy_agent(user_prompt)
    sidebar.title("Agent 1 response:")
    sidebar.markdown(f"Agent 1 response: {response_1}")

    response_2 = agent_2.deploy_agent(f"What the user initially asked: {user_prompt}. What Agent 1 proposes: {response_1}")
    sidebar.title("Agent 2 response:")
    sidebar.markdown(f"Agent 2 response: {response_2}")
    
    response_3 = agent_3.deploy_agent(f"What Agent 2 proposes: {response_2}")
    sidebar.title("Agent 3 response:")
    sidebar.markdown(f"Agent 3 response: {response_3}")

    response.write(response_3)