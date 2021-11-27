SURVEYS = {
    "survey1": {"id": 100, "name": "survey1"},
    "survey2": {"id": 200, "name": "survey2"},
}

QUESTIONS = {
    "survey1": [
        {"id": 101, "text": "Open ended"},
        {"id": 102, "text": "Multiple choice"},
        {"id": 103, "text": "Yes or no"},
    ],
    "survey2": [
        {"id": 201, "text": "Rating"},
        {"id": 202, "text": "Text"},
        {"id": 203, "text": "Number"},
    ],
}

RESPONSES = {
    "survey1": [
        {"id": 110, "session_id": "response110"},
        {"id": 120, "session_id": "response120"},
    ],
    "survey2": [
        {"id": 210, "session_id": "response210"},
        {"id": 220, "session_id": "response220"},
    ],
}

ANSWERS = {
    "response110": [
        {"id": 111, "response_id": 110, "question_id": 101, "text": "Blah"},
        {"id": 112, "response_id": 110, "question_id": 102, "text": "1"},
        {"id": 113, "response_id": 110, "question_id": 103, "text": "YES"},
    ],
    "response120": [
        {"id": 121, "response_id": 120, "question_id": 101, "text": "Blah"},
        {"id": 122, "response_id": 120, "question_id": 102, "text": "3"},
        {"id": 123, "response_id": 120, "question_id": 103, "text": "NO"},
    ],
    "response210": [
        {"id": 211, "response_id": 210, "question_id": 201, "text": "5"},
        {"id": 212, "response_id": 210, "question_id": 202, "text": "Sad"},
        {"id": 213, "response_id": 210, "question_id": 203, "text": "12"},
    ],
    "response220": [
        {"id": 221, "response_id": 220, "question_id": 201, "text": "5"},
        {"id": 222, "response_id": 220, "question_id": 202, "text": "Happy"},
        {"id": 223, "response_id": 220, "question_id": 203, "text": "7"},
    ],
}
