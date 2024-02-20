import os.path

from PageObject.logininpage import Loginpage
from PageObject.homepage import homepage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import ExcelUtilities
class Testloginpagedata:
    baseurl=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    path = os.path.abspath(os.curdir) + "/testdata" + "//testdatalogin.xlsx"

    # # Print out each component of the path
    # print("Current directory:", os.curdir)
    # print("Absolute path of current directory:", os.path.abspath(os.curdir))
    # print("Full path:", path)
    #
    # # Check if the directory exists
    # testdir = os.path.join(os.path.abspath(os.curdir), "testdata")
    # print("Is testdata directory present?", os.path.exists(testdir))
    #
    # # Check if the file exists
    # print("Is testdata_login.xlsx present?", os.path.exists(path))
    # print("Constructed path:", path)
    lst_status=[]
    def test_dataloginpage(self,setup):
        self.driver=setup
        self.logger.info("*******Launching application***********")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        #object for home page
        self.hp=homepage(self.driver)
        #object for loginpage
        rows=ExcelUtilities.getrowno(self.path,"Sheet1")

        for r in range(2,rows+1):
            self.lp = Loginpage(self.driver)
            self.hp.clicklogin()
            email_data=ExcelUtilities.readdata(self.path,"Sheet1",r,1)
            pwd_data=ExcelUtilities.readdata(self.path,"Sheet1",r,2)
            exp_result=ExcelUtilities.readdata(self.path,"Sheet1",r,3)
            self.lp.setemail(email_data)
            self.lp.setpassword(pwd_data)
            self.lp.clkloginbtn()
            target_page=self.lp.checktitle()
            if exp_result == True:
                if target_page == True:
                    self.lst_status.append("Passed")
                    self.lp.logout()
                    assert True
                else:
                    self.lst_status.append("Failed")
                    assert False
            elif exp_result == False:
                if target_page == True:
                    self.lst_status.append("Failed")
                    assert False
            else:
                self.lst_status.append("Passed")

            if exp_result != bool(target_page):
                continue



