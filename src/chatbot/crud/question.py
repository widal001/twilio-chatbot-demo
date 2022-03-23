from chatbot import schemas, models
from chatbot.crud.base import CRUDBase


class CRUDQuestion(
    CRUDBase[
        models.Question,
        schemas.QuestionIn,
        schemas.QuestionOut,
    ]
):
    """Manages CRUD operations for the Question table"""


question = CRUDQuestion(models.Question)
