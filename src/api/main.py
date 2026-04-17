from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Clinical Note Summarization API running"}

@app.get("/summarize")
def summarize():
    return {"summary": "Generated clinical summary"}
