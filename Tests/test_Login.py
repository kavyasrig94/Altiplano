from Utilities.BaseClass import BaseClass
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


class TestLogin(BaseClass):

    # def change_language(self):
    #     self.click_drop_down()
    #     self.select_eng_lang()
    #     assert  == 'English'

    def test_selectLang(self):
        log = self.getLogger()
        log.info("***************Testcase1 started******************")
        lp = LoginPage(self.driver)
        log.info("selcting the dropdown")
        lp.click_drop_down()
        log.info("drop down has been selected")
        lp.select_eng_lang()
        log.info("English language is selected")
        self.driver.refresh()
        assert True

    def test_login_Dx(self):
        log = self.getLogger()
        lp = LoginPage(self.driver)
        log.info("*************Testcase2 started**************")
        log.info("Trying to login")
        hp = lp.login("admin","Welcome1$")
        login_text_value = hp.logged_in_user()
        assert login_text_value == 'Logged in as admin', 'successfully loggedinn'

        # self.driver.find_element_by_xpath("//button[@class='btn btn-light dropdown-toggle dropdown-toggle-split']").click()
        # self.driver.find_element_by_id("langEn").click()
        # self.driver.refresh()
        # self.driver.find_element_by_name("username").send_keys("admin")
        # self.driver.find_element_by_name("password").send_keys("Welcome1$")
        # self.driver.find_element_by_id("loginBtn").click()
        # self.loginuser = self.driver.find_element_by_xpath("//a[text()='Logged in as admin']").text
        # if self.loginuser == 'Logged in as admin':
        #     print("login succsessful")













