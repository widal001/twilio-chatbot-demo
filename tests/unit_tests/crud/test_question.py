import pytest

from chatbot.crud.question import question
from tests.utils import data


class TestCRUDQuestion:
    """Tests the CRUDQuestion"""

    @pytest.mark.parametrize(
        "questions", [data.QUESTIONS["survey1"], data.QUESTIONS["survey2"]]
    )
    def test_get_question(self, questions, test_session):
        """Tests that the get() method executes successfully

        Validates the following conditions:
        - The correct question is returned
        - The next() method on the question returns the next question
          or None if the question is the last one in the survey
        """
        # execution
        for i, curr_q in enumerate(questions):
            next_q = questions[i]["id"] if i < len(questions) else None
            record = question.get(test_session, curr_q["id"])
            # validation
            assert record.id == curr_q["id"]
            assert record.text == curr_q["text"]
            if (i + 1) < len(questions):
                next_q = questions[i + 1]
                assert record.next().id == next_q["id"]
            else:
                assert record.next() is None
