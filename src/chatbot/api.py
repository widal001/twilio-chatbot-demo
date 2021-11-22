from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Basic router for testing"""
    return {"message": "Hello World"}


@app.get("/message")
def new_message():
    """The endpoint called by the Twilio webhook each time a new message is
    sent to the number reserved for this chatbot
    """
    return {"message": "Welcome to the survey"}


@app.get("/surveys/{survey_id}/questions/{question_id}")
def question(survey_id: int, question_id: int):
    """The endpoint that is called by the TwiML redirect function after a new
    survey is initiated or an answer to a survey question is processed
    """
    return {"survey": survey_id, "question": question_id}


@app.post(
    "/surveys/{survey_id}/questions/{question_id}/answers",
    status_code=201,
)
def answer(survey_id: int, question_id: int):
    """The endpoint that is called by the TwiML redirect function after a
    response to a survey question is received
    """
    return {"survey": survey_id, "answer": question_id}
