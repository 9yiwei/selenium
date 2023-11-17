from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __btn_locator = (By.ID, "add_btn")
    __row2_input_locator = (By.XPATH, "//div[@id='row2']//input[@class='input-field']")
    __row2_save_locator = (By.XPATH, "//div[@id='row2']//button[@name='Save']")
    __confirmation_locator = (By.ID, "confirmation")
    __row1_edit_locator = (By.ID, "edit_btn")
    __row1_input_locator = (By.XPATH, "//div[@id='row1']//input[@class='input-field']")
    __row1_save_locator = (By.XPATH, "//div[@id='row1']//button[@name='Save']")
    __instructions_locator = (By.ID, "instructions")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.open_url(self.__url)

    def add_btn(self):
        self.click(self.__btn_locator)
        self.visibility_of_element_wait(self.__row2_input_locator)

    def row2_is_displayed(self):
        return self.is_displayed(self.__row2_input_locator)

    def row2_type(self, text):
        self.type(self.__row2_input_locator, text)
        self.click(self.__row2_save_locator)
        self.visibility_of_element_wait(self.__confirmation_locator)

    def get_confirmation_text(self):
        return self.get_text(self.__confirmation_locator)

    def row1_edit(self):
        self.click(self.__row1_edit_locator)
        self.clickable_of_element_wait(self.__row1_input_locator)
        self.clear(self.__row1_input_locator)

    def row1_type(self, text):
        self.type(self.__row1_input_locator, text)
        self.click(self.__row1_save_locator)
        self.visibility_of_element_wait(self.__confirmation_locator)

    def row1_save(self):
        self.click(self.__row1_save_locator)

    def instructions_is_displayed(self):
        return self.is_displayed(self.__instructions_locator)

