from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
import time

class Profile_update:
    def __init__(self,driver):
        self.driver = driver

    def clickEditButton(self,edit_path):
        try:
            self.driver.find_element(By.XPATH, ReadConfig.get_chatbot_cancel_xpath()).click()
        except:
            pass
        self.driver.find_element(By.XPATH, edit_path).click()
        time.sleep(5)

    def clickSaveButton(self,save_path):
        self.driver.find_element(By.XPATH, save_path).click()

    def update_check(self,update_path):
        updatedate = self.driver.find_element(By.XPATH, update_path).text
        return updatedate

