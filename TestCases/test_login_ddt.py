import time
from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customLoger import LogGen
from utilities import XLutils

class Test_002_DDT_login:
    baseURL=Readconfig.getApplicationURL()
    path=".//TestData/TestData.xlsx"
    logger=LogGen.loggen()

    def test_DDT_login(self,setup):
        self.logger.info("**************** DDT_Login Test is passed************")
        self.logger.info("*******verify Login test is passed********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.rows=XLutils.getRowCount(self.path,'Sheet1')
        print("No of Rows:",self.rows)

        lst_status=[]
        for r in range(2,self.rows+1):
            self.username=XLutils.readData(self.path,'Sheet1',r,1)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.cliklogin()
            time.sleep(10)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce adminstration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Passed***")
                    self.lp.cliklogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***Failed***")
                    self.lp.cliklogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                        self.logger.info("***Failed***")
                        lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***Passed***")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
                self.logger.info("Login DDT Test Passed")
                self.driver.close()
                assert True

        else:
                self.logger.info("Login DDT Test Failed")
                assert False
        self.driver.close()
        self.logger.info("****END of login DDT Test*****")
        self.logger.info("*****Completed TC_002******")

