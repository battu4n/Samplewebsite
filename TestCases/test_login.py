from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customLoger import LogGen
import pytest

class Test_001_Login:
    baseURL=Readconfig.getApplicationURL()
    username= Readconfig.getUseremail()
    password = Readconfig.getPasswrd()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTittle(self,setup):
        self.logger.info("****************Test_001_Login************")
        self.logger.info("****************verify Home Page Tittle************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Home Page Tittle Test is pass************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homepagetittle.png")
            assert False
            self.driver.close()
            self.logger.error("**************** Home Page Tittle Test is Failed************")
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************** Login Test is Started************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.cliklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************** Login Test is pass************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "login.png")

            assert False
            self.driver.close()
            self.logger.error("**************** Login Test is Failed************")

