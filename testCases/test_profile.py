from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Profile_Update import Profile_update
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
import time

logger = LogGen.loggen('naukri_automation')

#@pytest.mark.usefixtures("browser_setup")
class Test_002_Profile:
    profile_url = ReadConfig.getprofile_url()
    fullname_xpath = ReadConfig.fullname_xpath()
    edit_xpath = ReadConfig.getedit_xpath()
    save = ReadConfig.getsave_xpath()
    updatedate = ReadConfig.getlastupdate_xpath()

    def test_profile_page(self,browser_setup):
        try:
            logger.info("*********************Test_002_Profile**************************************")
            logger.info("Verifying Profile page web elements ")
            self.driver = browser_setup
            self.driver.get(self.profile_url)
            element_user = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.fullname_xpath)))

            if self.driver.find_element(By.XPATH, self.fullname_xpath).text == "Sandeep Kumar Yadav":
                logger.info("Profile page web elements PASSED")
                assert True
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "profile_page_webelements.png")
                logger.info("Profile page web elements FAILED")
                assert False

        except Exception as e:
            logger.error(f"{str(e)}")


    def test_profile(self, browser_setup):
        try:
            logger.info("*********************Test_002_Profile**************************************")
            logger.info("Verifying Profile Update ")
            time.sleep(3)
            self.driver = browser_setup
            self.pu = Profile_update(self.driver)
            self.pu.clickEditButton(self.edit_xpath)
            self.pu.clickSaveButton(self.save)
            time.sleep(3)
            if self.pu.update_check(self.updatedate) == "Today" :
                print("Profile updated successfully!")
                logger.info("Profile Update test PASSED")
                #self.lp.logout()
                assert True
            else:
                print("Profile Update failed")
                self.driver.save_screenshot(".\\screenshots\\" + "test_profile.png")
                logger.info("Profile Update test FAILED")
                assert False

        except Exception as e:
            logger.error(f"{str(e)}")
            assert False