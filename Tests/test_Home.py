import pytest

from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Pages.HomePage import HomePage


class TestHome(BaseClass):

    def test_verify_dsllinks_text(self):
        log = self.getLogger()
        log.info("****************Home page test case started********************")
        lp= LoginPage(self.driver)
        lp.click_drop_down()
        lp.select_eng_lang()
        hp = lp.login("admin","Welcome1$")
        log.info("Getting the DSLlinks text")
        linkname = hp.dSlLinks()
        log.info("length of link names %s" , len(linkname))
        for i in range(0,len(linkname)):
            log.info("The linktext is  %s" , linkname[i].text)
            if linkname[i].text == "DSL" + str(i+1):
                assert True, "DSL link value is same"
            else:
                log.error("DSL values are not same")
                assert False, "DSL link values are not same"
        self.driver.quit()

    def test_dsl_links_validation(self):
        log = self.getLogger()
        log.info("****************Home page test case2 started********************")
        lp = LoginPage(self.driver)
        lp.click_drop_down()
        lp.select_eng_lang()
        hp = lp.login("admin", "Welcome1$")
        log.info("Getting the DSLlinks ")

        assert hp.validate_all_links() == 16, "16 DSL links are available"
