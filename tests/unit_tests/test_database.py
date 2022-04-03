from chatbot.models import Survey


def test_database(test_session):
    """Tests that the mock database was set up correctly"""
    # execute
    surveys = test_session.query(Survey).all()
    # validation
    assert len(surveys) == 2
    for survey in surveys:
        assert survey.name in ["survey1", "survey2"]
        assert len(survey.responses) == 2
        assert survey.questions.count() == 3  # needs count() b/c dynamic load
        assert survey.created_date is not None
