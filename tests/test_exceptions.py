import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

"""Test case 1: NoSuchElementException
Open page
Click Add button
Verify Row 2 input field is displayed
Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait"""
class TestException:
    @pytest.mark.exceptions
    @pytest.mark.positive
    def test_no_such_element_exception(self, driver):
        ### Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.ID, "add_btn").click()

        #driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row_2_input_element.is_displayed(), "Row2 is not displayed"



