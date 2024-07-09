import time
from selenium.webdriver.common.by import By
import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage

"""Test case 1: Positive LogIn test
Open page
Type username student into Username field
Type password Password123 into Password field
Push Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page"""

class TestPositiveScenerios:
    @pytest.mark.login
    @pytest.mark.positive_POM
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "URL is not correct"
        assert logged_in_page.header == "Congratulations" or "Logged In Successfully", "Header is not correct"
        assert logged_in_page.is_logout_button_displayed(), "Logout button is not displayed"
