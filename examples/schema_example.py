from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END

class InputState(TypedDict):
    user_input: str

class OutputState(TypedDict):
    graph_output: str

class OverallState(TypedDict):
    foo: str
    user_input:str
    graph_output: str

class PrivateState(TypedDict):
    bar: str

def node_1(state: InputState) -> OverallState:
    print(f'node 1: {state}')
    return {"foo": state["user_input"] + " name",
            "user_input": state["user_input"],
            "graph_output": "node_1"}

def node_2(state: OverallState) -> PrivateState:
    print(f'node 2: {state}')
    return {"bar": state["foo"] + " is"}

def node_3(state: PrivateState) -> OutputState:
    print(f'node 3: {state}')
    return {"graph_output": state["bar"] + " Lance"}


builder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

graph = builder.compile()
result = graph.invoke({"user_input": "My"})
print(f"result: {result}")