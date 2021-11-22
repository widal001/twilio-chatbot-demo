def test_root(mock_client):
    """Checks the `GET /` route

    Validates the following conditions:
    - The status returned is 200
    - The response data returned is "Hello Word"
    """
    # execution
    response = mock_client.get("/")
    # validation
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_message(mock_client):
    """Checks the `GET /message` route

    Validates the following conditions:
    - The status returned is 200
    - The response data returned is "Welcome to the survey"
    """
    # execution
    response = mock_client.get("/message")
    # validation
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the survey"}


def test_question(mock_client):
    """Checks the `GET /surveys/{survey_id}/questions/{question_id}` route

    Validates the following conditions:
    - The status returned is 200
    - The response data returned includes the survey and question id
    """
    # setup
    survey_id = 1
    question_id = 1
    url = f"/surveys/{survey_id}/questions/{question_id}"
    # execution
    response = mock_client.get(url)
    # validation
    assert response.status_code == 200
    assert response.json() == {"survey": survey_id, "question": question_id}


def test_answer(mock_client):
    """Checks the `GET /surveys/{survey_id}/questions/{question_id}` route

    Validates the following conditions:
    - The status returned is 201
    - The response data returned includes the survey and question id
    """
    # setup
    survey_id = 1
    question_id = 1
    url = f"/surveys/{survey_id}/questions/{question_id}/answers"
    # execution
    response = mock_client.post(url)
    print(response.json())
    # validation
    assert response.status_code == 201
    assert response.json() == {"survey": survey_id, "answer": question_id}
