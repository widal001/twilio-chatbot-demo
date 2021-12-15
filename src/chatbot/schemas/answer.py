from __future__ import annotations  # prevents NameError for typehints

from pydantic import BaseModel

from chatbot.schemas import OutMixin


class AnswerIn(BaseModel):
    response_id: int
    question_id: int
    text: str


class AnswerOut(AnswerIn, OutMixin):
    pass
