from selenium.webdriver.common.by import By
from selenium import webdriver

class HomePage:

    loginUser = (By.XPATH, "//a[text()='Logged in as admin']")

    def __init__(self, driver):
        self.driver = driver

    def logged_in_user(self):
        return self.driver.find_element(*HomePage.loginUser).text
