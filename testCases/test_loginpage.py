import os.path
import time

from PageObject.logininpage import Loginpage
from PageObject.homepage import homepage
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig

class TestLogin:
    baseurl=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    def test_loginpage(self,setup):
        self.driver=setup
        self.logger.info("***********Launching the application**********")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        #objectcreation for homepahe
        self.hp=homepage(self.driver)
        self.logger.info("Click on Login Button")
        self.hp.clicklogin()
        #object creation for loginpage
        self.lp=Loginpage(self.driver)
        self.logger.info("providing username")
        self.lp.setemail(ReadConfig.getusername())
        self.logger.info("providing password")
        self.lp.setpassword(ReadConfig.getpassword())
        self.logger.info("click on Remember me button")
        self.lp.clkremeberme()
        self.logger.info("click on login button")
        self.lp.clkloginbtn()
        if self.lp.checktitle()==True:
            assert True
            self.lp.logout()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//" + "test_login.png")
            assert False

