import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    print("Deepak")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\kg\\Documents\\selenium\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    #elif browser_name == "IE":
    #    print("IE driver")
    driver.get("https://135.249.28.70/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()



