from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph import add_messages
from langchain_openai import ChatOpenAI

class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)

llm = ChatOpenAI(
    api_key= "ollama",
    base_url= "http://localhost:11434/v1",
    model="deepseek-r1"
)

def chat(state: State) -> State:
    print(f"chat state: {state}")
    print("-----")
    return {"messages": [llm.invoke(state["messages"])]}

builder.add_node("chat", chat)
builder.add_edge(START, "chat")
builder.add_edge("chat", END)
graph = builder.compile()

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print(value)
            print("---------")
            print("Assistant:", value["messages"][-1].content)