from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import InMemorySaver

from  .types import State
from .nodes import (
    chat_node, 
    tool_chat_node, 
    tool_node,
    react_node
    )

memory = InMemorySaver()

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

def build_memory_tool_graph():
    builder = StateGraph(State)
    builder.add_edge(START, "tool_chat")
    builder.add_node("tool_chat", tool_chat_node)
    builder.add_node("tool_node", tool_node)
    builder.add_edge("tool_node", "tool_chat")
    return builder.compile(checkpointer=memory)

def build_react_graph():
    builder = StateGraph(State)
    builder.add_edge(START, "react_node")
    builder.add_node("react_node", react_node)
    return builder.compile()
