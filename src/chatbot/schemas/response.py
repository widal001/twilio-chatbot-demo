from __future__ import annotations  # prevents NameError for typehints
from typing import List

from pydantic import BaseModel

from chatbot.schemas import OutMixin, Answer


class ResponseBase(BaseModel):
    """Base schema for a response object"""

    session_id: str
    answers: List[Answer]


class Response(ResponseBase, OutMixin):
    """Serializes a survey response for the response body"""

    pass
