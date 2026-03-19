from fastapi import FastAPI
from pydantic import BaseModel
from main import run_agent


app=FastAPI()

class RequestModel(BaseModel):
    query: str
    session_id: str


@app.get("/")
def home():
    return {"message": "HybridAgentic AI is running 🚀"}


@app.post("/run-task")
def run_task(request: RequestModel):
    result=run_agent(request.query)
    return {"result": result}


