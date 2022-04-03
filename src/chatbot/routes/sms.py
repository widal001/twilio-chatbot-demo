from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from chatbot.crud import question, answer
from chatbot.db import get_db

router = APIRouter(prefix="/sms")


@router.get("/message")
def new_message():
    """Initiates survey loop

    This endpoint is called by the Twilio webhook when a new sms message is
    sent to the number reserved for this chatbot
    """
    return {"message": "Welcome to the survey"}


@router.get("/questions/{question_id}")
def get_question(question_id: int, db: Session = Depends(get_db)):
    """Prompts the user with the next question in the survey

    This endpoint is called by the TwiML redirect function when a new survey is
    initiated or after an answer to a previous question is recorded
    """
    record = question.get(db, question_id)
    return {"survey": record.survey_id, "question": record.id}


@router.post("/questions/{question_id}/answers", status_code=201)
def record_answer(
    question_id: int, answer_data: dict, db: Session = Depends(get_db)
):
    """Records the answer to a survey question

    This endpoint is called by the TwiML redirect function after a response to
    a survey question is received and it redirects to the question endpoint
    """
    curr_question = question.get(db, question_id)
    print(dir(answer))
    answer.save_response(db, curr_question, answer_data)
    next_question = curr_question.next()
    return {"current": curr_question.id, "next": next_question.id}
