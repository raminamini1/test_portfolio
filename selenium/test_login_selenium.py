# ============================================================
# Selenium WebDriver - UI Tests: Login-Formular
# Autor: Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM
# Framework: Selenium 4 + pytest
# Zweck: Browser-basierte Login-Tests mit Page Object Model (POM)
# ============================================================

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# ── Page Object: Login-Seite ─────────────────────────────────
class LoginPage:
    """Kapselt alle Elemente und Aktionen der Login-Seite (Page Object Model)."""

    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON  = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG    = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MSG      = (By.CSS_SELECTOR, ".flash.error")
    LOGOUT_BUTTON  = (By.XPATH, "//a[@href='/logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password: str):
        field = self.driver.find_element(*self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self

    def login(self, username: str, password: str):
        return self.enter_username(username).enter_password(password).click_login()

    def get_success_message(self) -> str:
        msg = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG))
        return msg.text

    def get_error_message(self) -> str:
        msg = self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
        return msg.text

    def is_success_message_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG))
            return True
        except Exception:
            return False

    def is_error_message_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
            return True
        except Exception:
            return False

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        return self


# ── Fixtures ─────────────────────────────────────────────────
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1400,900")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page


# ── Positive Tests ───────────────────────────────────────────
class TestLoginPositive:

    def test_successful_login_shows_success_message(self, login_page):
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert login_page.is_success_message_visible()

    def test_successful_login_message_text(self, login_page):
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in login_page.get_success_message()

    def test_logout_after_login(self, login_page):
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.click_logout()
        assert "login" in login_page.driver.current_url.lower()

    def test_page_title_on_load(self, login_page):
        assert "The Internet" in login_page.driver.title


# ── Negative Tests ───────────────────────────────────────────
class TestLoginNegative:

    def test_wrong_username_shows_error(self, login_page):
        login_page.login("wrong_user", "SuperSecretPassword!")
        assert login_page.is_error_message_visible()

    def test_wrong_password_shows_error(self, login_page):
        login_page.login("tomsmith", "falsch")
        assert login_page.is_error_message_visible()

    def test_empty_username_shows_error(self, login_page):
        login_page.login("", "SuperSecretPassword!")
        assert login_page.is_error_message_visible()

    def test_empty_password_shows_error(self, login_page):
        login_page.login("tomsmith", "")
        assert login_page.is_error_message_visible()

    def test_both_fields_empty_shows_error(self, login_page):
        login_page.login("", "")
        assert login_page.is_error_message_visible()


# ── Parametrisierter Test ────────────────────────────────────
@pytest.mark.parametrize("username, password", [
    ("wrong1", "wrong1"),
    ("wrong2", "wrong2"),
    ("",       "SuperSecretPassword!"),
    ("tomsmith", ""),
])
def test_invalid_logins_parametrized(login_page, username, password):
    login_page.login(username, password)
    assert login_page.is_error_message_visible()

# Terminal: pytest test_login_selenium.py -v
# pip install selenium pytest
