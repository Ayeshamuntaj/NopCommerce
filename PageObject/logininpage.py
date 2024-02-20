from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Loginpage:
    txt_email_xpath="//*[@id='Email']"
    txt_password_xpath="//*[@id='Password']"
    btn_rememberme_xpath="//*[@id='RememberMe']"
    btn_login_xpath="//*[@class='button-1 login-button']"
    img_title_xpath="/html/body/div[6]/div[1]/div[2]/div[1]/a/img"
    txt_logout_xpath="//*[@class='ico-logout']"
    #constructor
    def __init__(self,driver):
        self.driver=driver
    #action methods
    def setemail(self,email):
        email_input=self.driver.find_element(By.XPATH,self.txt_email_xpath)
        email_input.clear()
        email_input.send_keys(email)
    def setpassword(self, password):
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txt_password_xpath)))
        password_field.send_keys(password)
    def clkremeberme(self):
        self.driver.find_element(By.XPATH,self.btn_rememberme_xpath).click()
    def clkloginbtn(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
    def checktitle(self):
        try:
            return self.driver.find_element(By.XPATH,self.img_title_xpath).is_displayed()
        except:
            return False
    def logout(self):
        self.driver.find_element(By.XPATH,self.txt_logout_xpath).click()

