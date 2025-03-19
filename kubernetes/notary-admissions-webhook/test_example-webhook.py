
import pytest
from validation_webhook import app, validate_request

@pytest.fixture
def client():
    """ Creates a test client for Flask """
    app.config["TESTING"] = True
    return app.test_client()

def test_validate_request_success():
    """ Test when a valid request with 'example-label' is sent """
    valid_request = {
        "request": {
            "uid": "12345",
            "object": {
                "metadata": {
                    "labels": {
                        "example-label": "exists"
                    }
                }
            }
        }
    }
    
    response = validate_request(valid_request)
    assert response["response"]["allowed"] is True
    assert response["response"]["status"]["message"] == "Validation successful"

def test_validate_request_missing_label():
    """ Test when the required label is missing """
    invalid_request = {
        "request": {
            "uid": "12345",
            "object": {
                "metadata": {
                    "labels": {}
                }
            }
        }
    }

    response = validate_request(invalid_request)
    assert response["response"]["allowed"] is False
    assert response["response"]["status"]["message"] == "Missing required label: 'example-label'"

def test_validate_request_invalid_format():
    """ Test when an invalid request format is sent """
    invalid_request = {
        "request": {
            "uid": "12345",
            "object": {}
        }
    }

    response = validate_request(invalid_request)
    assert response["response"]["allowed"] is False
    assert "Error processing request" in response["response"]["status"]["message"]

def test_validate_endpoint(client):
    """ Test the /validate API endpoint with a valid request """
    valid_request = {
        "request": {
            "uid": "12345",
            "object": {
                "metadata": {
                    "labels": {
                        "example-label": "exists"
                    }
                }
            }
        }
    }

    response = client.post("/validate", json=valid_request)
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data["response"]["allowed"] is True
    assert json_data["response"]["status"]["message"] == "Validation successful"

def test_validate_endpoint_missing_label(client):
    """ Test the /validate API endpoint when label is missing """
    invalid_request = {
        "request": {
            "uid": "12345",
            "object": {
                "metadata": {
                    "labels": {}
                }
            }
        }
    }

    response = client.post("/validate", json=invalid_request)
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data["response"]["allowed"] is False
    assert json_data["response"]["status"]["message"] == "Missing required label: 'example-label'"
