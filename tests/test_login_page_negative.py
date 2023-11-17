import pytest
import time
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expect_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!")
                                 , ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expect_error_message):
        # 開啟頁面
        login_page = LoginPage(driver)
        login_page.open()
        # 在用戶名字段中輸入用戶名不正確的用戶
        # 在“密碼”欄位中輸入密碼“Password123”
        # 按下提交按鈕
        login_page.execute_login(username, password)
        # 驗證是否顯示錯誤訊息
        # 驗證錯誤訊息文字是您的使用者名稱無效！
        assert login_page.get_error_msg() == expect_error_message, "Error message is not expect."

        # # 開啟頁面
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        #
        # # 在用戶名字段中輸入用戶名不正確的用戶
        # user_locator = driver.find_element(By.ID, "username")
        # user_locator.send_keys(username)
        #
        # # 在“密碼”欄位中輸入密碼“Password123”
        # password_locator = driver.find_element(By.ID, "password")
        # password_locator.send_keys(password)
        #
        # # 按下提交按鈕
        # submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # submit_locator.click()
        # time.sleep(10)
        #
        # # 驗證是否顯示錯誤訊息
        # error_message_locator = driver.find_element(By.ID, "error")
        # assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be."
        #
        # # 驗證錯誤訊息文字是您的使用者名稱無效！
        # error_message = error_message_locator.text
        # assert error_message == expect_error_message, "Error message is not expect."
