from __future__ import annotations  # prevents NameError for typehints
from datetime import datetime

from fastapi import FastAPI

from chatbot import schemas

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
def get_question(survey_id: int, question_id: int):
    """The endpoint called by the TwiML redirect function after a new
    survey is initiated or an answer to a survey question is processed
    """
    return {"survey": survey_id, "question": question_id}


@app.post(
    "/surveys/{survey_id}/questions/{question_id}/answers",
    status_code=201,
)
def create_answer(survey_id: int, question_id: int):
    """The endpoint that is called by the TwiML redirect function after a
    response to a survey question is received
    """
    return {"survey": survey_id, "answer": question_id}


@app.post(
    "/surveys",
    response_model=schemas.SurveyQuestionsOut,
    status_code=201,
)
def create_survey(survey_data: schemas.SurveyQuestionsIn):
    """Create a new survey"""
    print(survey_data.name)
    result = {
        "id": 1,
        "name": "Welcome survey",
        "created_date": datetime(2021, 11, 2),
        "questions": [
            {
                "id": 1,
                "text": "Question 1",
                "created_date": datetime(2021, 11, 2),
            },
            {
                "id": 2,
                "text": "Question 2",
                "created_date": datetime(2021, 11, 2),
            },
        ],
    }
    response_data = schemas.SurveyQuestionsOut(**result)
    return response_data


@app.put("/surveys/{survey_id}", response_model=schemas.SurveyQuestionsOut)
def update_survey(survey_data: schemas.SurveyQuestionsIn):
    """Update the questions on an existing survey"""
    print(survey_data.name)
    result = {
        "id": 1,
        "name": "Welcome survey",
        "created_date": datetime(2021, 11, 2),
        "questions": [
            {
                "id": 1,
                "text": "Question 1",
                "created_date": datetime(2021, 11, 2),
            },
            {
                "id": 2,
                "text": "Question 2",
                "created_date": datetime(2021, 11, 2),
            },
        ],
    }
    response_data = schemas.SurveyQuestionsOut(**result)
    return response_data
