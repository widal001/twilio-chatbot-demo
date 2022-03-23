from __future__ import annotations  # prevents NameError for typehints

import chatbot.db.base as db


class Survey(db.Base):
    """Table that represents a collection of questions"""

    # columns
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.now())

    # relationships
    responses = db.relationship("Response", backref="survey")
    questions = db.relationship(
        "Question",
        backref="survey",
        lazy="dynamic",  # needed to make Question.next() filter work
    )
