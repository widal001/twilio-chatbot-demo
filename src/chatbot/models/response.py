from __future__ import annotations  # prevents NameError for typehints

import chatbot.database as db


class Response(db.Base):
    """Table that represents a collection of answers to a given survey"""

    __tablename__ = "response"

    # columns
    id = db.Column(db.Integer, primary_key=True, index=True)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"))
    session_id = db.Column(db.String)
    # start_time = db.Column(db.DateTime)
    # end_time = db.Column(db.DateTime)

    # relationship
    answers = db.relationship("Answer", backref="response")
