from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage


class LoginPage:
    dropdown = (By.XPATH, "//button[@class='btn btn-light dropdown-toggle dropdown-toggle-split']")
    dropdown_eng = (By.ID, "langEn")
    Nokialogo = (By.XPATH, "//img[@style= 'margin: 50px 0px']")
    usernametxtbox = (By.NAME, "username")
    passwordtxtbox = (By.NAME, "password")
    signinbutton = (By.ID, "loginBtn")
    Englishtext = (By.XPATH , '')


    def __init__(self,driver):
        self.driver = driver

    def click_drop_down(self):
        self.driver.find_element(*LoginPage.dropdown).click()

    def select_eng_lang(self):
        self.driver.find_element(*LoginPage.dropdown_eng).click()

    def login(self, un, pwd):
        self.driver.find_element(*LoginPage.usernametxtbox).send_keys(un)
        self.driver.find_element(*LoginPage.passwordtxtbox).send_keys(pwd)
        self.driver.find_element(*LoginPage.signinbutton).click()
        homePage = HomePage(self.driver)
        return homePage


    # def  logo_is_displayed(self):
    #     self.do_is_visibled(self.Nokialogo)




