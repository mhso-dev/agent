from functools import lru_cache

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from .tools import calculate, fake_search, get_time, multiply

TOOLS = [get_time, calculate, fake_search, multiply]


def build_agent():
    model = ChatOpenAI(model="gpt-4.1", temperature=0)
    try:
        model.bind_tools(TOOLS)
    except NotImplementedError:
        # LangChain's fake chat model used in tests does not implement tool binding.
        return create_agent(model=model, tools=[])

    return create_agent(model=model, tools=TOOLS)


@lru_cache
def get_agent():
    return build_agent()
