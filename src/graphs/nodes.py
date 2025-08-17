from typing import Literal
from langgraph.types import Command
from langgraph.prebuilt import ToolNode

from src.agents.agents import chat_agent, tool_chat_agent, react_agent
from src.tools import tavily_tool
from .types import State


def chat_node(state: State) -> Command[Literal["__end__"]]:
    response = chat_agent.invoke(state["messages"])

    return Command(
        update = {"messages": [response]},
        goto = "__end__",
    )

def tool_chat_node(state: State) -> Command[Literal["tool_node", "__end__"]]:
    response = tool_chat_agent.invoke(state["messages"])
    
    goto: Literal["tool_node", "__end__"] = "__end__"
    if ("tool_calls" in response.additional_kwargs) and (len(response.additional_kwargs["tool_calls"]) > 0):
        print(f"Tool Calls: {response.additional_kwargs['tool_calls']}")
        goto = "tool_node"

    return Command(
            update={"messages":[response]},
            goto=goto,
           )

tool_node = ToolNode([tavily_tool])

def react_node(state: State) -> Command[Literal["__end__"]]:
    response = react_agent.invoke(state["messages"])

    return Command(
        update= {"messages": [response]},
        goto="__end__",
    )