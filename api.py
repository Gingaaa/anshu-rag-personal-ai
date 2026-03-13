from fastapi import FastAPI
from pydantic import BaseModel
from main import chain, retriever

app = FastAPI()

class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(data: Question):
    docs = retriever.invoke(data.question)
    result = chain.invoke({
        "docs": docs,
        "question": data.question
    })

    return {
        "answer": result
    }