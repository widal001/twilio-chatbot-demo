from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from chatbot import schemas, models
from chatbot.crud.base import CRUDBase


class CRUDSurvey(
    CRUDBase[
        models.Survey,
        schemas.SurveyQuestionsIn,
        schemas.SurveyQuestionsIn,
    ]
):
    """Manages CRUD operations for the Survey table"""

    def create(
        self,
        db: Session,
        *,
        data: schemas.SurveyQuestionsIn,  # must be passed as keyword argument
    ) -> models.Survey:
        """Inserts a new row into the table that corresponds to the SQLAlchemy
        model being created

        Parameters
        ----------
        db: Session
            Instance of SQLAlchemy session that manages database transactions
        data: schemas.SurveyQuestionsIn
            The instance of the Pydantic schema that contains the data used to
            insert a new row in the database
        """
        survey_data = jsonable_encoder(data)
        question_data = survey_data.pop("questions")
        record = self.model(**survey_data)  # type: ignore
        for item in question_data:
            record.questions.append(models.Question(**item))
        return self.commit_changes(db, record)


survey = CRUDSurvey(models.Survey)
