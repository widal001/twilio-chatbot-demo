from __future__ import annotations  # prevents NameError for typehints
from typing import List

from pydantic import BaseModel

from chatbot.schemas import OutMixin, Answer


class QuestionIn(BaseModel):
    """Base schema for a question object which is also used to deserialize the
    question portion of the request body
    """

    text: str


class QuestionOut(QuestionIn, OutMixin):
    """Serializes a survey question for the response body"""

    pass


class QuestionResponses(QuestionOut):
    """Serializes a question for the response body along with its answers"""

    answers: List[Answer]
