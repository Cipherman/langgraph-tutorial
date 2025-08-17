from src.graphs.builder import build_tool_chat_graph

def main(graph):
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
            for value in event.values():
                print("Assistant", value["messages"][-1].content)

if __name__ == "__main__":
    graph = build_tool_chat_graph()
    main(graph)