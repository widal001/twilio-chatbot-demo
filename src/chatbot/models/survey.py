from __future__ import annotations  # prevents NameError for typehints

import chatbot.database as db


class Survey(db.Base):
    """Table that represents a collection of questions"""

    __tablename__ = "survey"

    # columns
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.now())

    # relationships
    questions = db.relationship("Question", backref="survey")
    responses = db.relationship("Response", backref="survey")
