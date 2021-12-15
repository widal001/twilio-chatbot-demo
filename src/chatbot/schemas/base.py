from __future__ import annotations  # prevents NameError for typehints
from datetime import datetime

from pydantic import BaseModel


class OutMixin(BaseModel):
    id: int
    created_date: datetime
