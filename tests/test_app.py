import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def app():
    with patch("app.get_db_connection"):
        from app import app as flask_app

        flask_app.config["TESTING"] = True
        return flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


@patch("app.get_click_count")
def test_index_page(mock_get_count, client):
    mock_get_count.return_value = 42

    response = client.get("/")
    assert response.status_code == 200
    assert b"Click Counter" in response.data
    assert b"42" in response.data


@patch("app.increment_click_count")
def test_click_endpoint(mock_increment, client):
    mock_increment.return_value = 100

    response = client.post("/click")
    assert response.status_code == 200
    assert response.json == {"clicks": 100}
    mock_increment.assert_called_once()


def test_routes_exist(app):
    rules = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/" in rules
    assert "/click" in rules
    assert "/health" in rules

