import json


def test_message(mock_client):
    """Tests GET /sms/message endpoint

    Validates the following conditions:
    - The status returned is 200
    - The response data returned is "Welcome to the survey"
    """
    # execution
    response = mock_client.get("/sms/message")
    # validation
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the survey"}


def test_question(mock_client):
    """Tests GET /sms/questions/{question_id} endpoint

    Validates the following conditions:
    - The status returned is 200
    - The response data returned includes the survey and question id
    """
    # setup
    survey_id = 100
    question_id = 101
    url = f"/sms/questions/{question_id}"
    # execution
    response = mock_client.get(url)
    # validation
    assert response.status_code == 200
    assert response.json() == {"survey": survey_id, "question": question_id}


def test_answer(mock_client):
    """Tests POST /sms/surveys/{survey_id}/questions/{question_id}/answers

    Validates the following conditions:
    - The status returned is 201
    - The response data returned includes the survey and question id
    """
    # setup
    question_id = 101
    answer_data = {"text": "Answer to question 1"}
    url = f"/sms/questions/{question_id}/answers"
    # execution
    response = mock_client.post(url, data=json.dumps(answer_data))
    print(response.json())
    # validation
    assert response.status_code == 201
    assert response.json() == {"current": question_id, "next": 102}
