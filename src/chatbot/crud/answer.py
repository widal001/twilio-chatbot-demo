from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from chatbot import schemas, models
from chatbot.crud.base import CRUDBase


class CRUDAnswer(
    CRUDBase[
        models.Question,
        schemas.QuestionIn,
        schemas.QuestionOut,
    ]
):
    """Manages CRUD operations for the Answer table"""

    def save_response(
        self,
        db: Session,
        question: models.Question,
        data: dict,
    ) -> None:
        """Records an answer to a survey question"""
        answer_data = jsonable_encoder(data)
        print(type(db))
        print(answer_data)
        print(question.text)


answer = CRUDAnswer(models.Answer)
