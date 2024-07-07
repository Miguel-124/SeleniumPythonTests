import pytest
from selenium import webdriver
@pytest.fixture()
def driver():
    print("Creating chrome driver instance")
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox() #--> Uncomment this line to run the tests in Firefox
    yield driver
    print("Closing chrome driver instance")
    driver.quit()