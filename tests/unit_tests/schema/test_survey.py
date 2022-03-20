import pytest
from pydantic.error_wrappers import ValidationError

import chatbot.schemas.survey as schemas


class TestSurveyQuestionsIn:
    """Tests the SurveyQuestionsIn schema"""

    def test_pass(self):
        """Tests that SurveyQuestionsIn passes with the correct input

        Validates the following conditions:
        - The pydantic schema is initialized without errors
        - All of the attributes are set correctly
        """
        # setup
        data_in = {
            "name": "Test Insert",
            "questions": [
                {"text": "Question 1"},
                {"text": "Question 2"},
                {"text": "Question 3"},
            ],
        }
        # execution
        output = schemas.SurveyQuestionsIn(**data_in)
        print(output)
        # validation
        assert output.name == data_in["name"]
        assert len(output.questions) == len(data_in["questions"])
        for i, question in enumerate(output.questions):
            assert question.text == data_in["questions"][i]["text"]

    def test_missing_questions(self):
        """Tests that SurveyQuestionsIn fails when it receives a survey without
        a set of questions
        """
        # setup
        data_in = {
            "name": "Test Insert",
        }
        # execution
        with pytest.raises(ValidationError):
            output = schemas.SurveyQuestionsIn(**data_in)
            print(output)
