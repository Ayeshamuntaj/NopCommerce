from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class accountregister:
    #locators
    radiobtn_gender_xpath="//*[@id='gender-male']"
    txtbox_fname_xpath="//*[@id='FirstName']"
    txtbox_lname_xpath="//*[@id='LastName']"
    select_date_xpath="//*[@name='DateOfBirthDay']"
    select_month_xpath="//*[@name='DateOfBirthMonth']"
    select_year_xpath="//*[@name='DateOfBirthYear']"
    txt_Email_xpath="//*[@id='Email']"
    txt_company_xpath="//*[@name='Company']"
    chkbox_newsletter_xpath="//*[@id='Newsletter']"
    txt_password_xpath="//*[@name='Password']"
    txt_confirmpassword_xpath="//*[@id='ConfirmPassword']"
    btn_continue_xpath="//*[@name='register-button']"
    txt_confirmmessage_xpath="//*[normalize-space()='Your registration completed']"
    btn_continue_regpage_xpath="//a[text()='Continue']"
    #constructors
    def __init__(self,driver):
        self.driver=driver
    #action methos
    def clickgender(self):
        self.driver.find_element(By.XPATH,self.radiobtn_gender_xpath).click()
    def setfirtname(self,fname):
        self.driver.find_element(By.XPATH,self.txtbox_fname_xpath).send_keys(fname)
    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txtbox_lname_xpath).send_keys(lname)
    def selectdate(self, date):
        self.datedrpdwn=Select(self.driver.find_element(By.XPATH,self.select_date_xpath))
        self.datedrpdwn.select_by_visible_text(date)
    def selectmonth(self, month):
        self.monthdrpdwn = Select(self.driver.find_element(By.XPATH, self.select_month_xpath))
        self.monthdrpdwn.select_by_visible_text(month)
    def selectyear(self, year):
        self.yeardrpdwn = Select(self.driver.find_element(By.XPATH, self.select_year_xpath))
        self.yeardrpdwn.select_by_visible_text(year)
    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)
    def setcompany(self, company):
        self.driver.find_element(By.XPATH, self.txt_company_xpath).send_keys(company)
    def clicknewsletter(self):
        self.driver.find_element(By.XPATH, self.chkbox_newsletter_xpath).click()
    def setpassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)
    def setconfirmpassword(self, confpwd):
        self.driver.find_element(By.XPATH, self.txt_confirmpassword_xpath).send_keys(confpwd)
    def clickcontinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
    def confirmmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_confirmmessage_xpath).text
        except:
            None
    def clickcontinueregpage(self):
        self.driver.find_element(By.XPATH, self.btn_continue_regpage_xpath).click()

