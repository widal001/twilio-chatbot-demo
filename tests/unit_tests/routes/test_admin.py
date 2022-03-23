import json


def test_create_survey(mock_client):
    """Tests the POST /survey endpoint"""
    # setup
    data = {
        "id": 1,
        "name": "Welcome survey",
        "questions": [
            {"id": 1, "text": "Question 1"},
            {"id": 2, "text": "Question 2"},
        ],
    }
    # execution
    response = mock_client.post(url="/admin/surveys", data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    # validation
    assert response.status_code == 201


def test_update_survey(mock_client):
    """Tests the PUT /admin/survey/{survey_id} endpoint"""
    # setup
    data = {
        "id": 1,
        "name": "Welcome survey",
        "questions": [
            {"id": 1, "text": "Question 1"},
            {"id": 2, "text": "Question 2"},
        ],
    }
    # execution
    response = mock_client.put(url="/admin/surveys/1", data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    # validation
    assert response.status_code == 200
