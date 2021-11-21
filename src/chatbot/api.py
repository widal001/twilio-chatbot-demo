from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Basic router for testing"""
    return {"message": "Hello World"}
