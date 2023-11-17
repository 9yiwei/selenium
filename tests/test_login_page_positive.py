import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        logged_successfully = LoggedInSuccessfullyPage(driver)
        # 找尋網頁
        login_page.open()
        # 輸入username
        # 輸入密碼
        # 按提交鈕
        login_page.execute_login("student", "Password123")
        # 驗證新頁面 URL 包含 practicetestautomation.com/logged-in-successively/
        assert logged_successfully.excepted_url == logged_successfully.current_url, \
            "Actual URL is not the same as expected."
        # 驗證新頁面包含預期文字（「恭喜」或「成功登入」）
        assert logged_successfully.header == "Logged In Successfully", "Header is not expected."
        # 驗證新頁面上是否顯示登出按鈕
        assert logged_successfully.is_logout_btn_displayed(), "Logout btn should be visible."

        # # 找尋網頁
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        #
        # # 輸入username
        # user_locator = driver.find_element(By.ID, "username")
        # user_locator.send_keys("student")
        #
        # # 輸入密碼
        # password_locator = driver.find_element(By.ID, "password")
        # password_locator.send_keys("Password123")
        #
        # # 按提交鈕
        # submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # submit_locator.click()
        # time.sleep(3)
        #
        # # 驗證新頁面 URL 包含 practicetestautomation.com/logged-in-successively/
        # actual_url = driver.current_url
        # assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        #
        # # 驗證新頁面包含預期文字（「恭喜」或「成功登入」）
        # # //div[@id='loop-container']//article//h1[@class='post-title']
        # text_locator = driver.find_element(By.TAG_NAME, "h1")
        # actual_text = text_locator.text
        # assert actual_text == "Logged In Successfully"
        #
        # # 驗證新頁面上是否顯示登出按鈕
        # # //div[@id='loop-container']//a[@class='wp-block-button__link has-text-color has-background
        # # has-very-dark-gray-background-color']
        # logout_locator = driver.find_element(By.LINK_TEXT, "Log out")
        # assert logout_locator.is_displayed()