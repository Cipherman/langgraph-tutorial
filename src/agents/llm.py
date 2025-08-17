from langchain_openai import ChatOpenAI

def create_openai_llm(
        model: str = "deepseek-r1",
        api_key: str = "ollama",
        base_url: str = "http://localhost:11434/v1",
        temperature: float = 0.1,
        **kwargs,
) -> ChatOpenAI:
    """ Create ChatOpenAI instance"""
    llm_kwargs = {"model": model, "temperature": temperature, **kwargs}

    if base_url:
        llm_kwargs["base_url"] = base_url

    if api_key:
        llm_kwargs["api_key"] = api_key

    return ChatOpenAI(**llm_kwargs)

llm = create_openai_llm()

if __name__ == "__main__":
    stream = llm.stream("how many 'r's are in 'strawberry'?")
    for chunk in stream:
        print(chunk.content, end="", flush=True)