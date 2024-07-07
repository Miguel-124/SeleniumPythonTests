import pytest
from selenium import webdriver
@pytest.fixture()
def driver():
    print("Creating chrome driver instance")
    driver = webdriver.Chrome()
    yield driver
    print("Closing chrome driver instance")
    driver.quit()