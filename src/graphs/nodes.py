from typing import Literal
from langgraph.types import Command

from src.agents.llm import llm
from .types import State

def chat_node(state: State) -> Command[Literal["__end__"]]:
    response = llm.invoke(state["messages"])

    return Command(
        update= {"messages": [response]},
        goto="__end__",
    )