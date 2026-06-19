from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field

from .agent import get_agent as get_cached_agent


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    answer: str


app = FastAPI(title="LLM Agent API")


def get_agent():
    return get_cached_agent()


agent_dependency = Depends(get_agent)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, agent=agent_dependency):
    result = await agent.ainvoke({"messages": [{"role": "user", "content": req.message}]})
    return ChatResponse(answer=result["messages"][-1].content)
