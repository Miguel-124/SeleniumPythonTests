from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.exceptions_page import ExceptionsPage


class TestException:
    """Test case 1: NoSuchElementException
    Open page
    Click Add button
    Verify Row 2 input field is displayed
    Row 2 doesn’t appear immediately.
    This test will fail with org.openqa.selenium.NoSuchElementException without proper wait"""
    @pytest.mark.exceptions_POM
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row2 is not displayed"

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
    @pytest.mark.exceptions_POM
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not expected"

    '''Test case 3: InvalidElementStateException
    Open page
    Clear input field
    Type text into the input field
    Verify text changed
    The input field is disabled. Trying to clear the disabled field will throw InvalidElementStateException. We need to enable editing of the input field first by clicking the Edit button.
    
    If we try to type text into the disabled input field, we will get ElementNotInteractableException, as in Test case 2.'''
    @pytest.mark.exceptions_POM
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row_1_input("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Confirmation message is not expected"

    '''Test case 4: StaleElementReferenceException
    Open page
    Find the instructions text element
    Push add button
    Verify instruction text element is no longer displayed
    The instructions element is removed from the page when the second row is added.
    That’s why we can no longer interact with it.
    Otherwise, we will see StaleElementReferenceException.'''

    @pytest.mark.exceptions_POM
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed(), "Instruction should not be displayed"


    '''Test case 5: TimeoutException
    Open page
    Click Add button
    Wait for 3 seconds for the second input field to be displayed
    Verify second input field is displayed
    The second row shows up after about 5 seconds, so a 3-second timeout is not enough. 
    That’s why we will get TimeoutException while executing steps in the above test case.'''

    @pytest.mark.exceptions_POM
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row2 is not displayed"