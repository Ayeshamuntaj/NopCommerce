import time
import os
from PageObject.homepage import homepage
from PageObject.Accountregister import accountregister
from Utilities import random_string
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Testacccountregister:
    baseurl=ReadConfig.getApplicationURL()
    def test_accountregister(self,setup):
        self.logger = LogGen.loggen()
        self.driver=setup
        self.logger.info("****Launching the test_Accountreg1 testcases ***************")
        self.driver.get(self.baseurl)
        self.logger.info("Launching the application")
        self.driver.maximize_window()
        #object for homepage
        self.hp=homepage(self.driver)
        self.logger.info("Land on to homepage")
        self.hp.clickregister()
        self.logger.info("click on register button")
        #object for accountregister
        self.logger.info("Land on Register page")
        self.accreg=accountregister(self.driver)
        self.logger.info("clicking gender button")
        self.accreg.clickgender()
        self.logger.info("providing firstname")
        self.accreg.setfirtname("John")
        self.logger.info("providing lastname")
        self.accreg.setlastname("Tester")
        self.logger.info("Select Date")
        self.accreg.selectdate("25")
        self.logger.info("Select month")
        self.accreg.selectmonth("July")
        self.logger.info("Select year")
        self.accreg.selectyear("1989")
        self.logger.info("Select email")
        self.email=random_string.random_string_generator()+"@gmail.com"
        self.accreg.setemail(self.email)
        self.logger.info("providing company name")
        self.accreg.setcompany("TESTING LTD")
        self.logger.info("click on newsletter")
        self.accreg.clicknewsletter()
        self.logger.info("providing password")
        self.accreg.setpassword("Test@12345")
        self.logger.info("providing confirm password")
        self.accreg.setconfirmpassword("Test@12345")
        self.logger.info("click on continue button")
        self.accreg.clickcontinue()
        self.logger.info("validating the confirmation message")
        if self.accreg.confirmmsg()=='Your registration completed':
            assert True
            self.accreg.clickcontinueregpage()
            self.driver.quit()
            self.logger.info("****test_Accountreg1 completed ***************")

        else:
            self.logger.info("confirmation message is wrong")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//" + "test_Accounteregister.png")
            self.driver.close()
            assert False
