from selenium.webdriver.common.by import By

from Pages.GenericPage import GenericPage


class LoginPage(GenericPage):
    dropdown = (By.XPATH, "//button[@class='btn btn-light dropdown-toggle dropdown-toggle-split']")
    dropdown_eng = (By.ID, "langEn")
    Nokialogo = (By.XPATH, "//img[@style= 'margin: 50px 0px']")
    usernametxtbox = (By.NAME, "username")
    passwordtxtbox = (By.NAME, "password")
    signinbutton = (By.ID, "loginBtn")

    def __init__(self,driver):
        super().__init__(driver)

    def click_drop_down(self):
        self.do_click(self.dropdown)

    def select_eng_lang(self):
        self.do_click(self.dropdown_eng)

    def login(self, un, pwd):
        self.do_send_keys(self.usernametxtbox, un)
        self.do_send_keys(self.passwordtxtbox, pwd)
        self.do_click(self.signinbutton)

    def  logo_is_displayed(self):
        self.do_is_visibled(self.Nokialogo)


