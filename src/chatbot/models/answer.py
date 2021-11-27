from __future__ import annotations  # prevents NameError for typehints

import chatbot.database as db


class Answer(db.Base):
    """Table that stores the answers to a question"""

    __tablename__ = "answer"

    # columns
    id = db.Column(db.Integer, primary_key=True, index=True)
    response_id = db.Column(db.Integer, db.ForeignKey("response.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    text = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=db.func.now())
