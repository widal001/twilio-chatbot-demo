from __future__ import annotations  # prevents NameError for typehints
from typing import List

from pydantic import BaseModel

from chatbot.schemas import OutMixin, AnswerOut


class ResponseBase(BaseModel):
    session_id: str
    answers: List[AnswerOut]


class Response(ResponseBase, OutMixin):
    pass
