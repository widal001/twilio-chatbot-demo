from __future__ import annotations
from typing import Iterable

from sqlalchemy.orm import Session

from chatbot import models
from tests.utils import data


def add_to_session(session: Session, entries: Iterable) -> None:
    """Adds uncommitted schema objects to the session

    Parameters
    ----------
    session: Session
        The SQLAlchemy session to add the items to before committing
    entries: Iterable
        An iterable of instances of SQLAlchemy models to add to the session
    """
    for entry in entries:
        session.add(entry)


def populate_db(session: Session) -> None:
    """Populates the mock database with test data

    Parameters
    ----------
    session: Session
        A SQLAlchemy session object passed to this function by the fixture
    """
    # init surveys
    surveys = {k: models.Survey(**v) for k, v in data.SURVEYS.items()}
    add_to_session(session, surveys.values())

    # add questions and responses to survey
    for survey, item in surveys.items():
        item.questions = [models.Question(**q) for q in data.QUESTIONS[survey]]
        item.responses = [models.Response(**r) for r in data.RESPONSES[survey]]

    # init answers
    for response in data.ANSWERS.values():
        records = [models.Answer(**answer) for answer in response]
        add_to_session(session, records)

    session.commit()
