from __future__ import annotations  # prevents NameError for typehints
from typing import List

from pydantic import BaseModel

from chatbot.schemas import OutMixin, QuestionIn, QuestionOut, Response


class SurveyBase(BaseModel):
    """Base schema for survey"""

    name: str


class SurveyQuestionsIn(SurveyBase):
    """Deserializes the request body when creating or updating a survey"""

    questions: List[QuestionIn]


class SurveyQuestionsOut(SurveyBase, OutMixin):
    """Serializes a survey and its questions for a response body"""

    questions: List[QuestionOut]


class SurveyResponsesOut(SurveyBase, OutMixin):
    """Serializes a survey and its responses for a response body"""

    responses: List[Response]
