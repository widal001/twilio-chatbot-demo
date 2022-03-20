from chatbot.crud.survey import survey
from chatbot.schemas.survey import SurveyQuestionsIn
from tests.utils import data


class TestCRUDSurvey:
    """Tests the CRUDSurvey"""

    def test_create_success(self, test_session):
        """Tests that the create() method executes successfully

        Validates the following conditions:
        - The survey is created without raising errors
        - The survey attributes matchc the input
        - The survey includes the correct set of questions
        - All of the objects that were created have ids
        """
        # setup
        survey_data = {
            "name": "Test Insert",
            "questions": [
                {"text": "Question 1"},
                {"text": "Question 2"},
                {"text": "Question 3"},
            ],
        }
        survey_in = SurveyQuestionsIn(**survey_data)
        # execute
        output = survey.create(test_session, data=survey_in)
        print(output.name)
        print(output.id)
        # validate
        assert output.name == survey_in.name
        assert output.id is not None
        for i, question in enumerate(output.questions):
            assert survey_in.questions[i].text == question.text
            assert question.id is not None

    def test_get(self, test_session):
        """Tests the get() method executes successfully

        Validates the following conditions:
        - Method retrieves a survey record without error
        - The record returned is the correct record
        """
        # setup
        exp_survey = data.SURVEYS["survey1"]
        exp_questions = data.QUESTIONS["survey1"]
        # execution
        output = survey.get(test_session, exp_survey["id"])
        print(output.name)
        print(output.id)
        # validation
        assert output.id == exp_survey["id"]
        assert output.name == exp_survey["name"]
        for i, question in enumerate(output.questions):
            assert question.id == exp_questions[i]["id"]
            assert question.text == exp_questions[i]["text"]


class TestGetMany:
    """Tests the get_many() method"""

    def test_get_many_default(self, test_session):
        """Tests the get_many() method"""
        # setup
        expected = list(data.SURVEYS.values())
        # execution
        output = survey.get_many(test_session)
        print(output)
        # validation
        assert len(output) == len(expected)
        for i, record in enumerate(output):
            assert record.name == expected[i]["name"]

    def test_get_many_skip(self, test_session):
        """Tests the get_many() method with skip parameter"""
        # setup
        expected = data.SURVEYS["survey2"]
        # execution
        output = survey.get_many(test_session, skip=1)
        print(output)
        print(expected)
        # validation
        assert len(output) == 1
        assert output[0].id == expected["id"]

    def test_get_many_limit(self, test_session):
        """Tests the get_many() method with skip parameter"""
        # setup
        expected = data.SURVEYS["survey1"]
        # execution
        output = survey.get_many(test_session, limit=1)
        print(output)
        print(expected)
        # validation
        assert len(output) == 1
        assert output[0].id == expected["id"]


class TestDelete:
    """Tests the delete() method"""

    def test_delete(self, test_session):
        """Tests the delete() method operates successfully

        Validates the following conditions:
        - The survey record is successfully deleted
        - The related questions are also deleted
        """
        # execution
        output = survey.delete(test_session, id=100)
        print(output)
        print(output.id)
        # validation
        surveys = survey.get_many(test_session)
        assert 100 not in [r.id for r in surveys]
