import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # 開啟頁面
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 點擊新增按鈕
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 驗證第 2 行輸入欄位是否顯示
        wait = WebDriverWait(driver, 10)
        input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']")))
        assert input_locator.is_displayed(), "Row 2 input should be display, but it's not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # 開啟頁面
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 點擊新增按鈕
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 等待第二行加載
        wait = WebDriverWait(driver, 10)
        input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']//"
                                                                             "input[@class='input-field']")))
        assert input_locator.is_displayed(), "Row 2 input should be display, but it's not"

        # 在第二個輸入欄位中輸入文字
        input_locator.send_keys("Curry")

        # 使用定位器
        save_locator = driver.find_element(By.XPATH, "//div[@id='row2']//button[@name='Save']")

        # By.name(“Save”) 按下“儲存”按鈕
        save_locator.click()

        # 驗證文字已儲存
        confirmation_locator = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_locator.text
        assert confirmation_message == "Row 2 was saved", "Row 2 text should be display, but it's not"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # 開啟頁面
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        wait = WebDriverWait(driver, 10)
        # 清除輸入字段
        edit_locator = driver.find_element(By.ID, "edit_btn")
        edit_locator.click()
        input_locator = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='row1']//"
                                                                         "input[@class='input-field']")))
        input_locator.clear()
        # 在輸入欄位中輸入文字
        input_locator.send_keys("Curry")
        save_locator = driver.find_element(By.XPATH, "//div[@id='row1']//button[@name='Save']")
        save_locator.click()

        # 驗證文字已更改
        text = input_locator.get_attribute("value")
        assert text == "Curry", f"Excepted Curry, but got {text}."

    @pytest.mark.exceptions
    def test_tale_element_reference_exception(self, driver):
        # 開啟頁面
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 尋找說明文字元素
        dir_locator = driver.find_element(By.ID, "instructions")
        assert dir_locator.is_displayed(), "dir should be display, but it's not."

        # 按下新增按鈕
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 驗證說明文字元素不再顯示
        # try:
        #     dir_locator
        # except NoSuchElementException:
        #     print("Because you touch Add button, so dir disappear.")
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")), "dir should not be display.")

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # 開啟頁面
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # 點擊新增按鈕
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # 等待 3 秒顯示第二個輸入字段
        wait = WebDriverWait(driver, 6)
        input_locator = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']")),
                                   "Time out!!")

        # 驗證第二個輸入欄位是否顯示
        assert input_locator.is_displayed()