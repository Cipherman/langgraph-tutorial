from langgraph.graph import StateGraph, START

from  .types import State
from .nodes import chat_node

def build_graph():
    builder = StateGraph(State)
    builder.add_edge(START, "chat")
    builder.add_node("chat", chat_node)
    return builder.compile()
