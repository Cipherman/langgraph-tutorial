from src.graphs.builder import build_memory_tool_graph

def main(graph):
    while True:
        user_id = input("User ID: ")
        config = {"configurable": {"thread_id": user_id}}
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        events =  graph.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            config,
            stream_mode="values",
        )
        for event in events:
            event["messages"][-1].pretty_print()
            #for value in event.values():
            #    print("Assistant", value["messages"][-1].content)

if __name__ == "__main__":
    graph = build_memory_tool_graph()
    main(graph)