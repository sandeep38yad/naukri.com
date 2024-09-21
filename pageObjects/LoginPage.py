from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import time
class LoginPage:
    username_xpath = ReadConfig.getuserxpath()
    pass_xpath = ReadConfig.getpassxpath()
    submit_xpath = ReadConfig.getsubmitxpath()
    bar_xpath = ReadConfig.getbarxpath()
    logout_xpath = ReadConfig.getlogoutxpath()


    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.pass_xpath).send_keys(password)

    def submit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.bar_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        print("Clicked logout")
        time.sleep(3)
