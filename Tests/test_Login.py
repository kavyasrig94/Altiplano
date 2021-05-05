from Utilities.BaseClass import BaseClass
from selenium import webdriver
import pytest

# dropdown = (By.XPATH, "//button[@class='btn btn-light dropdown-toggle dropdown-toggle-split']")
# dropdown_eng = (By.ID, "langEn")
# Nokialogo = (By.XPATH, "//img[@style= 'margin: 50px 0px']")
# usernametxtbox = (By.NAME, "username")
# passwordtxtbox = (By.NAME, "password")
# signinbutton = (By.ID, "loginBtn")
# Englishtext = (By.XPATH, '')

class Login(BaseClass):

    # def change_language(self):
    #     self.click_drop_down()
    #     self.select_eng_lang()
    #     assert  == 'English'

    def test_selectlang(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-light dropdown-toggle dropdown-toggle-split']").click()
        self.driver.find_element_by_id("langEn").click()
        self.driver.find_element_by_name("username").sendkeys("admin")
        self.driver.find_element_by_name("password").sendkeys("Welcome1$")
        self.driver.find_element_by_id("loginBtn").click()
        self.driver.find_element_by_linktext("Logged in as admin")











