from typing import Annotated
from operator import add

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END

#class State(TypedDict):
#    foo: int
#    bar: list[str]

class State(TypedDict):
    foo: int
    bar: Annotated[list[str], add]

def node_1(state: State) -> State:
    print(f"node 1: {state}")
    return {"foo": 2}

def node_2(state: State) -> State:
    print(f"node 2: {state}")
    return {"bar": ["bye"]}

builder= StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", END)

graph = builder.compile()
result = graph.invoke({"foo": 1, "bar":["hi"]})
print(f'result: {result}')