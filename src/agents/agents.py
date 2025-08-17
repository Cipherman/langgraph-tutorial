from src.tools import tavily_tool
from .llm import llm

def create_chat():
    return llm

def creat_tool_chat():
    return llm.bind_tools([tavily_tool])

chat_agent = create_chat()
tool_chat_agent = creat_tool_chat()