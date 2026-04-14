# ============================================================
# Playwright - Moderne UI-Tests: Login-Formular
# Autor: Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM
# Framework: Playwright (Python) + pytest-playwright
# Zweck: Schnelle, zuverlaessige Browser-Tests mit Auto-Wait
# ============================================================

import pytest
from playwright.sync_api import Page, expect

URL = "https://the-internet.herokuapp.com/login"
VALID_USER = "tomsmith"
VALID_PASS = "SuperSecretPassword!"


def do_login(page: Page, username: str, password: str):
    """Navigiert zur Login-Seite und fuellt das Formular aus."""
    page.goto(URL)
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")


# ── Positive Tests ───────────────────────────────────────────
class TestLoginPositive:

    def test_successful_login(self, page: Page):
        """Gueltige Zugangsdaten -> Erfolgsmeldung sichtbar."""
        do_login(page, VALID_USER, VALID_PASS)
        success = page.locator(".flash.success")
        expect(success).to_be_visible()
        expect(success).to_contain_text("You logged into a secure area!")

    def test_page_url_after_login(self, page: Page):
        """Nach Login -> URL enthaelt 'secure'."""
        do_login(page, VALID_USER, VALID_PASS)
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    def test_logout_redirects_to_login(self, page: Page):
        """Login -> Logout -> zurueck auf Login-Seite."""
        do_login(page, VALID_USER, VALID_PASS)
        page.click("a[href='/logout']")
        expect(page).to_have_url(URL)

    def test_login_page_title(self, page: Page):
        """Titel der Login-Seite korrekt."""
        page.goto(URL)
        expect(page).to_have_title("The Internet")

    def test_username_field_is_visible(self, page: Page):
        """Username-Feld ist sichtbar beim Oeffnen."""
        page.goto(URL)
        expect(page.locator("#username")).to_be_visible()

    def test_password_field_is_visible(self, page: Page):
        """Passwort-Feld ist sichtbar beim Oeffnen."""
        page.goto(URL)
        expect(page.locator("#password")).to_be_visible()


# ── Negative Tests ───────────────────────────────────────────
class TestLoginNegative:

    def test_wrong_username_shows_error(self, page: Page):
        """Falscher Nutzername -> Fehlermeldung."""
        do_login(page, "wrong_user", VALID_PASS)
        expect(page.locator(".flash.error")).to_be_visible()

    def test_wrong_password_shows_error(self, page: Page):
        """Falsches Passwort -> Fehlermeldung."""
        do_login(page, VALID_USER, "falsches_passwort")
        expect(page.locator(".flash.error")).to_be_visible()

    def test_empty_username_shows_error(self, page: Page):
        """Leeres Namensfeld -> Fehlermeldung."""
        do_login(page, "", VALID_PASS)
        expect(page.locator(".flash.error")).to_be_visible()

    def test_empty_password_shows_error(self, page: Page):
        """Leeres Passwortfeld -> Fehlermeldung."""
        do_login(page, VALID_USER, "")
        expect(page.locator(".flash.error")).to_be_visible()

    def test_both_fields_empty_shows_error(self, page: Page):
        """Beide Felder leer -> Fehlermeldung."""
        do_login(page, "", "")
        expect(page.locator(".flash.error")).to_be_visible()


# ── Parametrisierter Test (Data-Driven) ──────────────────────
@pytest.mark.parametrize("username, password", [
    ("falsch",    "falsch"),
    ("",           VALID_PASS),
    (VALID_USER,   ""),
    ("sql'--",     "injection"),
    ("<script>",   "<script>"),
])
def test_invalid_combinations(page: Page, username: str, password: str):
    """Data-Driven: Verschiedene ungueltige & sicherheitskritische Eingaben."""
    do_login(page, username, password)
    expect(page.locator(".flash.error")).to_be_visible()


# ── Ausfuehren ────────────────────────────────────────────────
# Terminal:  pytest test_login_playwright.py -v
# pip install pytest-playwright && playwright install chromium
# Headed:    pytest test_login_playwright.py --headed
# Firefox:   pytest test_login_playwright.py --browser firefox
