from __future__ import annotations  # prevents NameError for typehints

import chatbot.db.base as db


class Question(db.Base):
    """Table that contains the questions that comprise a given survey"""

    # columns
    id = db.Column(db.Integer, primary_key=True, index=True)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"))
    text = db.Column(db.String)
    created_date = db.Column(db.DateTime)

    # relationships
    answers = db.relationship("Answer", backref="question")

    def next(self):
        """Returns the next question in the survey"""
        questions = self.survey.questions
        return questions.filter(Question.id > self.id).order_by("id").first()
