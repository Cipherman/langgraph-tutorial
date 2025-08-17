from langgraph.prebuilt import create_react_agent

from src.tools import tavily_tool
from .llm import llm

def create_chat_agent():
    return llm

def creat_tool_chat_agent():
    return llm.bind_tools([tavily_tool])

chat_agent = create_chat_agent()

tool_chat_agent = creat_tool_chat_agent()

react_agent = create_react_agent(
    model = llm,
    tools=[tavily_tool],
    prompt="always check the current time first."
)