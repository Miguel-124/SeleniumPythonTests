import time
from selenium.webdriver.common.by import By
import pytest


class TestNegativeScenerios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        ### Open page
        # driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        ###Type username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        ###Type password into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        ###Push Submit button
        subbmit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        subbmit_button_locator.click()
        time.sleep(2)

        ###Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"

        ###Verify error message text!
        assert error_message_locator.text == expected_error_message, "Error message is not correct"

    # --> The following test cases are not needed anymore, because they are covered by the parametrized test above

    # """Test case 2: Negative username test
    # Open page
    # Type username incorrectUser into Username field
    # Type password Password123 into Password field
    # Push Submit button
    # Verify error message is displayed
    # Verify error message text is Your username is invalid!"""
    #
    # def test_negative_username(self, driver):
    #     ### Open page
    #     # driver = webdriver.Chrome()
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #
    #     ###Type username incorrectUser into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("incorrectUser")
    #
    #     ###Type password Password123 into Password field
    #     password_locator = driver.find_element(By.NAME, "password")
    #     password_locator.send_keys("Password123")
    #
    #     ###Push Submit button
    #     subbmit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
    #     subbmit_button_locator.click()
    #     time.sleep(2)
    #
    #     ###Verify error message is displayed
    #     error_message_locator = driver.find_element(By.ID, "error")
    #     assert error_message_locator.is_displayed(), "Error message is not displayed"
    #
    #     ###Verify error message text is Your username is invalid!
    #     assert error_message_locator.text == "Your username is invalid!", "Error message is not correct"
    #
    # """Test case 3: Negative password test
    # Open page
    # Type username student into Username field
    # Type password incorrectPassword into Password field
    # Push Submit button
    # Verify error message is displayed
    # Verify error message text is Your password is invalid!"""
    #
    # def test_negative_password(self, driver):
    #     ### Open page
    #     # driver = webdriver.Chrome()
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #
    #     ###Type username student into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("student")
    #
    #     ###Type password incorrectPassword into Password field
    #     password_locator = driver.find_element(By.NAME, "password")
    #     password_locator.send_keys("incorrectPassword")
    #
    #     ###Push Submit button
    #     subbmit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
    #     subbmit_button_locator.click()
    #     time.sleep(2)
    #
    #     ###Verify error message is displayed
    #     error_message_locator = driver.find_element(By.ID, "error")
    #     assert error_message_locator.is_displayed(), "Error message is not displayed"
    #
    #     ###Verify error message text is Your password is invalid!
    #     assert error_message_locator.text == "Your password is invalid!", "Error message is not correct"
