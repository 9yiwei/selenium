from selenium.webdriver.common.by import By


class LoggedInSuccessfullyPage:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __text_locator = (By.TAG_NAME, "h1")
    __logout_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.__url)

    @property
    def excepted_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return self.driver.find_element(self.__text_locator).text

    # 此為檢查該button是否存在，是一個動作/一瞬間的事，故不適合使用property
    def is_logout_btn_displayed(self) -> bool:
        return self.driver.find_element(self.__logout_locator).is_displayed()