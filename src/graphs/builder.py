from langgraph.graph import StateGraph, START

from  .types import State
from .nodes import chat_node, tool_chat_node, tool_node

def build_chat_graph():
    builder = StateGraph(State)
    builder.add_edge(START, "chat")
    builder.add_node("chat", chat_node)
    return builder.compile()

def build_tool_chat_graph():
    builder = StateGraph(State)
    builder.add_edge(START, "tool_chat")
    builder.add_node("tool_chat", tool_chat_node)
    builder.add_node("tool_node", tool_node)
    builder.add_edge("tool_node", "tool_chat")
    return builder.compile()
