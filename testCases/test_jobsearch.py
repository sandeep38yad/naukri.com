from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.jobsearch import jobs
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.db_insert import insertDB
import pytest
import time
import json

logger = LogGen.loggen('naukri_automation')

class Test_003_Jobsearch:

    # keywords = ReadConfig.getkeyword().split(",")
    job_count_xpath = ReadConfig.job_count_xpath()
    pagecount_xpath = ReadConfig.getpagecount_xpath()
    nextpage_xpath = ReadConfig.getnextpage_xpath()
    complete_details = []


    def next_page_availibility(self):
        next = True
        try:
            nextPage = self.driver.find_element(By.XPATH, self.pagecount_xpath)
            next = False
            print("Reached end of page")
        except:
            pass
        return next

    def start_processing(self, keyword, yoe, page):
        try:
            #for yoe in range(0, 3):
                if page == 1:
                    self.jb.send_keywords_in_searchbar(keyword, yoe)
                # self.jb.submit()
                available_jobs = self.driver.find_elements(By.XPATH, self.job_count_xpath)
                print(f'{len(available_jobs)} jobs found')
                # if len(list(available_jobs)) > 0 :
                #    count += 1
                if len(available_jobs) > 0:
                    try:
                        self.complete_details += self.jb.collect_details(available_jobs)

                    except Exception as e:
                        print(f'Error in start_processing {str(e)}')

        except Exception as e:
            print(f'Error in start_processing: {str(e)}')

    def test_qa_avaialable_jobs(self, browser_setup):
        try:
            logger.info("*********************Test_003_avaialable_jobs**************************************")
            logger.info("Searching available jobs ")
            # with open(r'./testCases/traversed.txt', 'w', encoding='utf-8') as f1:
            #     pass
            self.driver = browser_setup
            self.jb = jobs(self.driver)

            for keyword in ReadConfig.getkeyword('qa').split(","):
                for yoe in range(0, 3):
                    print(f'Checking for {keyword}|{yoe} exp.')
                    page = 1
                    self.start_processing(keyword, yoe, page)

                    while self.next_page_availibility():
                        if page > 15:
                            break
                        try:
                            page += 1
                            self.driver.find_element(By.XPATH, self.nextpage_xpath).click()
                            print(f".................................Clicked page [{page}]...............................")
                            time.sleep(2)
                            self.start_processing(keyword, yoe, page)
                        except Exception as e:
                            print(f'Error in while loop test_avaialable_jobs:{str(e)}')

            # with open(r'./testCases/jobdetails.json', 'w', encoding='utf-8') as file:
            #     json.dump(self.complete_details, file, indent=4)

        except Exception as e:
            print(f'Error in test_avaialable_jobs:{str(e)}')
            logger.error(f'Error in test_avaialable_jobs:{str(e)}')

