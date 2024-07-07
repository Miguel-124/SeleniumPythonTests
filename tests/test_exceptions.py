import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestException:
    """Test case 1: NoSuchElementException
    Open page
    Click Add button
    Verify Row 2 input field is displayed
    Row 2 doesn’t appear immediately.
    This test will fail with org.openqa.selenium.NoSuchElementException without proper wait"""
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        ### Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.ID, "add_btn").click()

        #driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row_2_input_element.is_displayed(), "Row2 is not displayed"

    '''Test case 2: ElementNotInteractableException
    Open page
    Click Add button
    Wait for the second row to load
    Type text into the second input field
    Push Save button using locator By.name(“Save”)
    Verify text saved
    This page contains two elements with attribute name=”Save”.
    The first one is invisible. So when we are trying to click on the invisible element, we get ElementNotInteractableException.
    
    The same action used to throw ElementNotVisibleException, but now it throws a different exception (not sure if it’s a bug in Selenium or a feature)'''
    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        ### Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        row_2_input_element.send_keys("Sushi")

        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()
        assert driver.find_element(By.ID, "confirmation").text == "Row 2 was saved", "Row 2 was not saved"

    '''Test case 3: InvalidElementStateException
    Open page
    Clear input field
    Type text into the input field
    Verify text changed
    The input field is disabled. Trying to clear the disabled field will throw InvalidElementStateException. We need to enable editing of the input field first by clicking the Edit button.
    
    If we try to type text into the disabled input field, we will get ElementNotInteractableException, as in Test case 2.'''
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        ### Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.ID, "edit_btn").click()
        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((row_1_input_element))).clear()
        row_1_input_element.send_keys("Sushi")

        driver.find_element(By.ID, "save_btn").click()

        #WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "confirmation")))
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "confirmation"))).text == "Row 1 was saved", "Row 1 was not saved"
