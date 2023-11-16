import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Excepted 'Chrome' or 'Firefox', but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.quit()
    print(f"Quiting {browser} driver")


# 自定義--browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
    )