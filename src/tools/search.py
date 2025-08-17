import os
from langchain_tavily import TavilySearch


os.environ["TAVILY_API_KEY"] = "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"

tavily_tool = TavilySearch(max_results=2)

if __name__ == "__main__":
    result = tavily_tool.invoke("What's the best practice for organizing an LangGraph Project?")
    print(result)