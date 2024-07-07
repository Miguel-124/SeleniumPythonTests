import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    #browser = request.config.getoption("--browser")
    browser = request.param
    print(f"Creating {browser} driver instance")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{browser} is not supported!")
    yield driver
    print(f"Closing {browser} driver instance")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")