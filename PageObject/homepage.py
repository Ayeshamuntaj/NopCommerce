from selenium import webdriver
from selenium.webdriver.common.by import By

class homepage:
    #locators
    txt_Registor_xpath="//*[@class='ico-register']"
    txt_login_xpath="//*[@class='ico-login']"

    #constructors
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def clickregister(self):
        self.driver.find_element(By.XPATH,self.txt_Registor_xpath).click()
    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.txt_login_xpath).click()