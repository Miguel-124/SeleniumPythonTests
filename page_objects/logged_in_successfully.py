from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginInSuccessfullyPage:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __logout_button_locator = (By.LINK_TEXT, "Log out")
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header_text(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    @property
    def logout_button(self) -> bool:
        return self._driver.find_element(self.__logout_button_locator).is_displayed()
