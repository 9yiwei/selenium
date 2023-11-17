from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, text: str, time: int = 10,):
        self._visibility_of_element_wait(locator, time)
        self._find(locator).send_keys(text)

    def click(self, locator: tuple, time: int = 10,):
        self._visibility_of_element_wait(locator, time)
        self._find(locator).click()

    def _visibility_of_element_wait(self, locator: tuple, time: int = 10,):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located(self._find(locator)))

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def open_url(self, url: str):
        self.driver.get(url)

    def get_text(self, locator: tuple, time: int = 10,):
        self._visibility_of_element_wait(locator, time)
        return self._find(locator).text

