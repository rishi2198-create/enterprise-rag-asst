from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Asst",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Enterprise RAG Asst"
    }
