from __future__ import annotations  # prevents NameError for typehints
from datetime import datetime

from pydantic import BaseModel


class OutMixin(BaseModel):
    """Base schema to serialize objects with id and created_date"""

    id: int
    created_date: datetime
