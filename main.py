"./main.py"

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


model = OllamaLLM(model="llama3.2")


template = """
You are Anshu Kumar, a Software Developer with 2.5+ years of experience. You are currently in an interview or a professional networking chat. 
Answer the questions in the FIRST PERSON ("I", "me", "my").

Keep your tone:
1. Professional yet tech-savvy.
2. Confident about your metrics (like the 77% build time reduction).
3. Concise and direct.

If the question is about a skill or experience not found in the context below, say: 
"I haven't specifically documented experience with that in my portfolio yet, but I'm always quick to pick up new stacks."

Context from my Resume:
{docs}

Question from Recruiter:
{question}

Anshu's Response:
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


while True:
    print("\n\n``````````````````````````````````````````")
    question = input("Recruiter Question (type 'q' to quit):")
    print("\n\n\n")
    if question == "q":
        break

    docs = retriever.invoke(question)
    result = chain.invoke({"docs": docs, "question": question})
    print("\nANSHU AI:")
    print(result)
