from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
import time

logger = LogGen.loggen('naukri_automation')

#@pytest.mark.usefixtures("browser_setup")
class Test_001_Login():
    base_url = ReadConfig.getbase_url()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    username_xpath = ReadConfig.getuserxpath()
    pass_xpath = ReadConfig.getpassxpath()

    def test_login_page_webelements(self,browser_setup):
        try:
            logger.info("*********************Test_001_Login**************************************")
            logger.info("Verifying login page web elements ")
            self.driver = browser_setup
            self.driver.get(self.base_url)
            element_user = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.username_xpath)))
            element_pass = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.pass_xpath)))

            if element_user and element_pass:
                logger.info("login page web elements PASSED")
                assert True
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "login_page_webelements.png")
                logger.info("login page web elements FAILED")
                assert False
        except Exception as e:
            logger.error("{str(e)}")

    def test_login(self, browser_setup):
        try:
            logger.info("*********************Test_001_Login**************************************")
            logger.info("Verifying Login ")
            time.sleep(3)
            self.driver = browser_setup
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.submit()
            time.sleep(3)
            if "homepage" in self.driver.title.lower() or "home" in self.driver.title.lower():
                print("Login successful!")
                logger.info("Login test PASSED")
                #self.lp.logout()
                assert True
            else:
                print("Login failed")
                print(self.driver.title.lower())
                self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
                logger.info("Login test FAILED")
                assert False

        except Exception as e:
            logger.error(f"{str(e)}")
            assert False




