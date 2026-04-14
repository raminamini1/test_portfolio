# ============================================================
# pytest - API Tests: Login-Endpunkt
# Autor: Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM
# Framework: pytest + requests
# Zweck: REST-API Login-Endpunkt testen (Demo: reqres.in)
# ============================================================

import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.fixture
def valid_credentials():
    return {"email": "eve.holt@reqres.in", "password": "cityslicka"}


@pytest.fixture
def invalid_credentials():
    return {"email": "wrong@test.de", "password": "falsch"}


class TestLoginPositive:

    def test_login_returns_200(self, valid_credentials):
        """Erfolgreicher Login gibt HTTP 200 zurueck."""
        response = requests.post(f"{BASE_URL}/login", json=valid_credentials)
        assert response.status_code == 200

    def test_login_returns_token(self, valid_credentials):
        """Antwort enthaelt einen Token."""
        response = requests.post(f"{BASE_URL}/login", json=valid_credentials)
        data = response.json()
        assert "token" in data
        assert len(data["token"]) > 0

    def test_response_time_under_2_seconds(self, valid_credentials):
        """API muss innerhalb von 2 Sekunden antworten (Performance)."""
        response = requests.post(f"{BASE_URL}/login", json=valid_credentials)
        assert response.elapsed.total_seconds() < 2.0


class TestLoginNegative:

    def test_login_invalid_credentials_returns_400(self, invalid_credentials):
        """Falsche Zugangsdaten -> HTTP 400."""
        response = requests.post(f"{BASE_URL}/login", json=invalid_credentials)
        assert response.status_code == 400

    def test_login_missing_password_returns_error(self):
        """Fehlendes Passwort -> Fehlermeldung in der Antwort."""
        response = requests.post(f"{BASE_URL}/login", json={"email": "test@test.de"})
        data = response.json()
        assert "error" in data

    def test_login_empty_body_returns_400(self):
        """Leerer Body -> HTTP 400."""
        response = requests.post(f"{BASE_URL}/login", json={})
        assert response.status_code == 400


# Terminal: pytest test_login_api.py -v
# pip install requests pytest
