from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest
import time

logger = LogGen.loggen('naukri_automation')

@pytest.mark.usefixtures("browser_setup")
class Test_002_ddt_Login:
    base_url = ReadConfig.getbase_url()
    username_xpath = ReadConfig.getuserxpath()
    pass_xpath = ReadConfig.getpassxpath()
    xl_path = './/TestData/LoginData.xlsx'

    def test_login_ddt(self):
        try:
            logger.info("*********************Test_002_ddt_Login**************************************")
            logger.info("Verifying Login ")
            time.sleep(3)
            self.lp = LoginPage(self.driver)
            self.rows = XLUtils.getRowCount(self.xl_path, "Sheet1")
            test_result = []
            for r in range(2, self.rows+1):
                self.driver.get(self.base_url)
                time.sleep(5)
                self.user = XLUtils.readData(self.xl_path, "Sheet1", r, 1)
                self.passwd = XLUtils.readData(self.xl_path, "Sheet1", r, 2)
                self.exp = XLUtils.readData(self.xl_path, "Sheet1", r, 3)
                self.lp.setUserName(self.user)
                self.lp.setPassword(self.passwd)
                self.lp.submit()
                time.sleep(3)

                title = self.driver.title.lower()
                if "homepage" in title or "home" in title:
                    print("Login successful!")
                    if self.exp == "Pass":
                        test_result.append("Pass")
                        logger.info("PASSED")
                    elif self.exp == "Fail":
                        test_result.append("Fail")

                elif "homepage" not in title and "home" not in title:
                    print("Login failed")
                    if self.exp == "Fail":
                        print(self.driver.title.lower())
                        test_result.append("Pass")
                        logger.info("PASSED")
                    elif self.exp == "Pass":
                        print(self.driver.title.lower())
                        test_result.append("Fail")
                try:
                    self.lp.logout()
                except:
                    pass

            if "Fail" not in test_result and len(test_result) == self.rows - 1:
                logger.info("********* Login DDT test PASSED ***********")
                assert True
            else:
                logger.info("********* Login DDT test PASSED ************")
                assert False

            logger.info("****** End of login DDT test *********")
            logger.info("****** Completed Test_002_ddt_Login **********")

        except Exception as e:
            print(f"{str(e)}")
            logger.error(f"{str(e)}")
            assert False




