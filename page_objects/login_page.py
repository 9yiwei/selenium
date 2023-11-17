from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_btn = (By.XPATH, "//button[@class='btn']")
    __error_msg = (By.ID, "error")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.open_url(self.__url)

    def execute_login(self, username, password):
        self.type(self.__username_field, username)
        self.type(self.__password_field, password)
        self.click(self.__submit_btn)

    def get_error_msg(self) -> str:
        return self.get_text(self.__error_msg, time=3)

        # wait = WebDriverWait(self.driver, 10)
        # # 輸入username
        # wait.until(ec.visibility_of_element_located(self.__username_field))
        # self.driver.find_element(self.__username_field).send_keys(username)
        #
        # # 輸入密碼
        # wait.until(ec.visibility_of_element_located(self.__password_field))
        # self.driver.find_element(self.__password_field).send_keys(password)
        #
        # # 按提交鈕
        # wait.until(ec.visibility_of_element_located(self.__submit_btn))
        # self.driver.find_element(self.__submit_btn).click()