import time
from selenium.webdriver.common.by import By
import pytest

from page_objects.login_page import LoginPage

"""Test case 1: Positive LogIn test
Open page
Type username student into Username field
Type password Password123 into Password field
Push Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page"""


class LoggedInSuccessfullyPage:
    pass


class TestPositiveScenerios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "URL is not correct"
        assert logged_in_page.header == "Congratulations" or "Logged In Successfully", "Header is not correct"
        assert logged_in_page.logout_button(), "Logout button is not displayed"

        # ### Open page
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        #
        # ###Type username student into Username field
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys("student")
        #
        # ###Type password Password123 into Password field
        # password_locator = driver.find_element(By.NAME, "password")
        # password_locator.send_keys("Password123")
        #
        # ###Push Submit button
        # subbmit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # subbmit_button_locator.click()
        # time.sleep(2)
        #
        # ###Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url
        #
        # ###Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # logging_successful_locator = driver.find_element(By.TAG_NAME, "h1")
        # assert "Congratulations" or "Logged In Successfully" in logging_successful_locator.text
        #
        # ###Verify button Log out is displayed on the new page
        # logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        # assert logout_button_locator.is_displayed()