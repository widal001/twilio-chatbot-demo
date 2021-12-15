from __future__ import annotations  # prevents NameError for typehints
from typing import List

from pydantic import BaseModel

from chatbot.schemas import OutMixin, QuestionIn, QuestionOut, Response


class SurveyBase(BaseModel):
    name: str


class SurveyQuestionsIn(SurveyBase):
    questions: List[QuestionIn]


class SurveyQuestionsOut(SurveyBase, OutMixin):
    questions: List[QuestionOut]


class SurveyResponsesOut(SurveyBase, OutMixin):
    responses: List[Response]
