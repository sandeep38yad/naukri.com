from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import ignore_company_list
import time
from datetime import datetime
import re

logger = LogGen.loggen('naukri_automation')

class jobs:
    searchbar_xpath = ReadConfig.getsearchbarxpath()
    keywordxpath = ReadConfig.getkeywordxpath()
    yoexpath = ReadConfig.getyoexpath()
    yoe = ReadConfig.getyoe()
    submit_xpath = ReadConfig.getsubmit_xpath()
    freshness_xpath = ReadConfig.getfreshness_xpath()
    freshness_dropdown = ReadConfig.getfreshness_dropdown_xpath()
    companyName_xpath = ReadConfig.getcompany_xpath()
    remote_xpath = ReadConfig.getremote_xpath()
    location_xpath = ReadConfig.getlocation_xpath()
    apply_xpath = ReadConfig.getapply_xpath()
    direct_apply_xpath = ReadConfig.get_direct_apply_xpath()
    chatbot_close_xpath = ReadConfig.chatbot_close_xpath()
    job_link_xpath = ReadConfig.getjob_link_xpath()
    jd_xpath = ReadConfig.getjd_xpath()

    def __init__(self, driver):
        self.driver = driver
        self.complete_job_details = []

    def send_keywords_in_searchbar(self,keyword,yoe):
        try:
            self.driver.find_element(By.XPATH, self.searchbar_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.keywordxpath).send_keys((Keys.CONTROL + 'a', Keys.BACKSPACE))
            self.driver.find_element(By.XPATH, self.keywordxpath).send_keys(keyword)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.yoexpath).click()
            time.sleep(2)
            yoe_dropdown_xpath = self.yoe.replace("0", str(yoe))
            self.driver.find_element(By.XPATH, yoe_dropdown_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.submit_xpath).click()
            time.sleep(2)
            new_url = self.driver.current_url + "&jobAge=1"
            self.driver.get(new_url)

            # element_user = WebDriverWait(self.driver, 30).until(
            #     EC.presence_of_element_located((By.XPATH, self.freshness_xpath)))
            #
            # self.driver.find_element(By.XPATH, self.freshness_dropdown).click()
            # self.driver.find_element(By.XPATH, self.freshness_xpath).click()
            time.sleep(2)

        except Exception as e:
            print(f'Error in send_keywords_in_searchbar: {str(e)}')
            logger.error(f'Error in send_keywords_in_searchbar: {str(e)}')

    def getTitle(self):
        try:
            title_xpath = ReadConfig.get_title_xpath()
            title = self.driver.find_element(By.XPATH, title_xpath)
            return title.text
        except Exception as e:
            print(f'Error in getTitle: {str(e)}')
            return False

    def req_exp(self):
        try:
            exp_xpath = ReadConfig.get_jobExp_xpath()
            exp = self.driver.find_element(By.XPATH, exp_xpath)
            total_exp = exp.text.split("years")
            if "-" in total_exp[0]:
                min_exp = total_exp[0].split("-")[0].strip()
                max_exp = total_exp[0].split("-")[1].strip()
            else:
                min_exp = 0
                max_exp = 0
            return int(min_exp), int(max_exp)
        except Exception as e:
            print(f'Error in req_exp: {str(e)}')
            return False

    def get_company_name(self):
        try:
            company = self.driver.find_element(By.XPATH, self.companyName_xpath).text
            return company
        except Exception as e:
            print(f'Error in get_company_name: {str(e)}')
            return False

    def getLocation(self):
        try:
            try:
                locaton = []
                loc = self.driver.find_element(By.XPATH, self.remote_xpath).text
                locaton.append(loc)

            except:
                loc = self.driver.find_elements(By.XPATH, self.location_xpath)
                for l in loc:
                    if l.text:
                        locaton.append(l.text)

            return locaton
        except Exception as e:
            print(f'Error in getLocation: {str(e)}')
            return False

    def check_direct_apply(self,title):
        try:
            qa_titles = ReadConfig.get_title_keywords('qa').split(",")
            pattern = '|'.join(qa_titles)
            if re.search(pattern, title, re.IGNORECASE):
                self.driver.find_element(By.XPATH, self.direct_apply_xpath).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.chatbot_close_xpath).click()
        except Exception as e:
            pass
    def get_apply_link(self, title):
        try:
            self.driver.find_element(By.XPATH, self.apply_xpath).click()
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            applyURL = self.driver.current_url
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            return applyURL

        except Exception as e:
            #print(f'Error in get_apply_link: {str(e)}')
            # self.check_direct_apply(title)
            return "Not Found"

    def get_full_jd(self):
        try:
            jd = self.driver.find_element(By.XPATH, self.jd_xpath).text
            return jd
        except Exception as e:
            #print(f'Error in  getting full jd:{str(e)}')
            return "Not Available"

    def traversed(self, job, jobno):
        try:
            joblink = job.find_elements(By.XPATH, '//a[@class="title "]' ) #self.job_link_xpath)
            line = joblink[jobno].get_attribute('href')
            title = joblink[jobno].get_attribute('title')
            with open('./testCases/traversed.txt', 'r', encoding='utf-8') as f1:
                lines = f1.readlines()
            lines = {url.split()[2] for url in lines}
            if line in lines:
                print(f'Already traversed: {line}')
                return True
            if line not in lines:
                companies = ignore_company_list()
                pattern = '|'.join(companies)
                if re.search(pattern, line, re.IGNORECASE):
                    print(f'Mass recruiter so ignoring.....')
                    return True

            qa_titles = ReadConfig.get_title_keywords('qa').split(",")
            pattern = '|'.join(qa_titles)
            if re.search(pattern, title, re.IGNORECASE):
                current_time = datetime.now()
                with open('./testCases/traversed.txt', 'a+', encoding='utf-8') as f1:
                    print(str(current_time) + "  " + line, file=f1)
                return False
            else:
                print("Other department job so skipping......")
                return True

        except Exception as e:
            print(f'Error in traversed:{str(e)}')
            return False

    def collect_details(self, available_jobs):
        jobno = 0
        for job in available_jobs:
            try:
                if self.traversed(job, jobno):
                    continue
                jobno += 1
                job.click()
                time.sleep(2)
                all_windows = self.driver.window_handles
                #WebDriverWait(self.driver, 15).until(EC.new_window_is_opened(all_windows))
                self.driver.switch_to.window(all_windows[-1])

                documents_dict = {}
                title = self.getTitle()
                min_exp, max_exp = self.req_exp()
                print(f'Title: {title}')
                documents_dict['title'] = title
                print(f'Exp: {min_exp}-{max_exp} years')
                documents_dict['min_exp'] = min_exp
                documents_dict['max_exp'] = max_exp
                company = self.get_company_name()
                print(f'Company: {company}')
                documents_dict['company'] = company
                location = self.getLocation()
                print(f'Location: {location}')
                documents_dict['location'] = location
                apply_link = self.get_apply_link(title)
                print(f'Apply: {apply_link}')
                documents_dict['apply_link'] = apply_link
                full_jd = self.get_full_jd()
                # print(f'FULL_JD: {full_jd}')
                documents_dict['full_jd'] = full_jd
                if self.driver.window_handles[0] != self.driver.window_handles[-1]:
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    self.complete_job_details.append(documents_dict)

            except Exception as e:
                print(f'Error in collect_details: {str(e)}')
                if self.driver.window_handles[0] != self.driver.window_handles[-1]:
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])

        return self.complete_job_details

    def submit(self):
        try:
            self.driver.find_element(By.XPATH, self.submit_xpath).click()

        except Exception as e:
            print(f'Error in submit:{str(e)}')
