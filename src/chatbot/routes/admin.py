from datetime import datetime

from fastapi import APIRouter

from chatbot import schemas

router = APIRouter(prefix="/admin")


@router.post(
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


@router.put("/surveys/{survey_id}", response_model=schemas.SurveyQuestionsOut)
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
