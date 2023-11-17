from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __text_locator = (By.TAG_NAME, "h1")
    __logout_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.open_url(self.__url)

    @property
    def excepted_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return self.get_text(self.__text_locator)

    # 此為檢查該button是否存在，是一個動作/一瞬間的事，故不適合使用property
    def is_logout_btn_displayed(self) -> bool:
        return self.is_displayed(self.__logout_locator)

