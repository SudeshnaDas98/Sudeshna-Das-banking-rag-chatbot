from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from main import ask_chatbot

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "Banking Chatbot API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(req: ChatRequest):

    answer = ask_chatbot(req.query)

    return {
        "query": req.query,
        "answer": answer
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    return {
        "filename": file.filename,
        "message": "File uploaded successfully"
    }
