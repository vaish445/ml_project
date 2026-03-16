from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Model API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}
