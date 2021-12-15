from __future__ import annotations  # prevents NameError for typehints

from pydantic import BaseModel

from chatbot.schemas import OutMixin


class AnswerBase(BaseModel):
    """Base schema for an answer object"""

    response_id: int
    question_id: int
    text: str


class Answer(AnswerBase, OutMixin):
    """Serializes an answer object for the response body"""

    pass
