import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# Test case 1: Positive LogIn test
class TestPositiveScenerios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        ### Open page
        # Open browser
        driver = webdriver.Chrome()
        time.sleep(2)

        # Open URL
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        ###Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        ###Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        ###Push Submit button
        subbmit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        subbmit_button_locator.click()
        time.sleep(2)

        ###Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url

        ###Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        logging_successful_locator = driver.find_element(By.TAG_NAME, "h1")
        assert "Congratulations" or "Logged In Successfully" in logging_successful_locator.text

        ###Verify button Log out is displayed on the new page
        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.is_displayed()

