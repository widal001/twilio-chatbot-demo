from fastapi import APIRouter

router = APIRouter(prefix="/sms")


@router.get("/message")
def new_message():
    """Initiates survey loop

    This endpoint is called by the Twilio webhook when a new sms message is
    sent to the number reserved for this chatbot
    """
    return {"message": "Welcome to the survey"}


@router.get("/surveys/{survey_id}/questions/{question_id}")
def get_question(survey_id: int, question_id: int):
    """Prompts the user with the next question in the survey

    This endpoint is called by the TwiML redirect function when a new survey is
    initiated or after an answer to a previous question is recorded
    """
    return {"survey": survey_id, "question": question_id}


@router.post(
    "/surveys/{survey_id}/questions/{question_id}/answers",
    status_code=201,
)
def create_answer(survey_id: int, question_id: int):
    """Records the answer to a survey question

    This endpoint is called by the TwiML redirect function after a response to
    a survey question is received and it redirects to the question endpoint
    """
    return {"survey": survey_id, "answer": question_id}
