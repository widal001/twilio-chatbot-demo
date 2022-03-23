from fastapi import FastAPI

from chatbot.routes import sms, admin

app = FastAPI()
app.include_router(sms.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    """Basic router for testing"""
    return {"message": "Hello World"}
