from __future__ import annotations  # prevents NameError for typehints
from typing import List

from pydantic import BaseModel

from chatbot.schemas import OutMixin, AnswerOut


class QuestionIn(BaseModel):
    text: str


class QuestionOut(QuestionIn, OutMixin):
    pass


class QuestionResponses(QuestionOut):
    answers: List[AnswerOut]
