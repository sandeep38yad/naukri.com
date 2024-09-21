import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getbase_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getusername():
        user = config.get('common info', 'username')
        return user

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getuserxpath():
        uxpath = config.get('common info', 'username_xpath')
        return uxpath

    @staticmethod
    def getpassxpath():
        pxpath = config.get('common info', 'pass_xpath')
        return pxpath

    @staticmethod
    def getsubmitxpath():
        sxpath = config.get('common info', 'submit_xpath')
        return sxpath

    @staticmethod
    def getbarxpath():
        bxpath = config.get('common info', 'bar_xpath')
        return bxpath

    @staticmethod
    def getlogoutxpath():
        lxpath = config.get('common info', 'logout_xpath')
        return lxpath

    @staticmethod
    def getprofile_url():
        url = config.get('profile section', 'profile_url')
        return url

    @staticmethod
    def fullname_xpath():
        name = config.get('profile section', 'fullname_xpath')
        return name

    @staticmethod
    def getedit_xpath():
        edit = config.get('profile section', 'edit_xpath')
        return edit

    @staticmethod
    def getsave_xpath():
        save = config.get('profile section', 'save_xpath')
        return save

    @staticmethod
    def getlastupdate_xpath():
        update = config.get('profile section', 'last_update_xpath')
        return update

    @staticmethod
    def chatbot_close_xpath():
        chatbot = config.get('profile section', 'chatbot_xpath')
        return chatbot

    @staticmethod
    def getsearchbarxpath():
        searchbar = config.get('jobsearch section', 'searchbar_xpath')
        return searchbar

    @staticmethod
    def getkeywordxpath():
        keywordxpath = config.get('jobsearch section', 'keyword_xpath')
        return keywordxpath
    @staticmethod
    def getkeyword():
        keyword = config.get('jobsearch section', 'keyword')
        return keyword

    @staticmethod
    def getyoexpath():
        yoexpath = config.get('jobsearch section', 'yoe_xpath')
        return yoexpath

    @staticmethod
    def getyoe():
        yoe = config.get('jobsearch section', 'yoe_dropdown_xpath')
        return yoe

    @staticmethod
    def getsubmit_xpath():
        submit = config.get('jobsearch section', 'submitxpath')
        return submit

    @staticmethod
    def getfreshness_xpath():
        fresh = config.get('jobsearch section', 'freshxpath')
        return fresh

    @staticmethod
    def job_count_xpath():
        count = config.get('jobsearch section', 'job_count_xpath')
        return count

    @staticmethod
    def getpagecount_xpath():
        page = config.get('jobsearch section', 'pagecount_xpath')
        return page

    @staticmethod
    def getnextpage_xpath():
        next = config.get('jobsearch section', 'nextpage_xpath')
        return next

    @staticmethod
    def get_title_xpath():
        title = config.get('jobdetail section', 'titlexpath')
        return title

    @staticmethod
    def get_jobExp_xpath():
        exp_xpath = config.get('jobdetail section', 'expxpath')
        return exp_xpath

    @staticmethod
    def getfreshness_dropdown_xpath():
        dropdown_xpath = config.get('jobsearch section', 'fresh_dropdown_xpath')
        return dropdown_xpath

    @staticmethod
    def getjob_link_xpath():
        job_link_xpath = config.get('jobsearch section', 'each_job_xpath')
        return job_link_xpath
    @staticmethod
    def getcompany_xpath():
        comp_xpath = config.get('jobdetail section', 'companyxpath')
        return comp_xpath

    @staticmethod
    def getjd_xpath():
        jd_xpath = config.get('jobdetail section', 'full_jd')
        return jd_xpath


    @staticmethod
    def getremote_xpath():
        remote_xpath = config.get('jobdetail section', 'remote_xpath')
        return remote_xpath

    @staticmethod
    def getlocation_xpath():
        loc_xpath = config.get('jobdetail section', 'location_xpath')
        return loc_xpath

    @staticmethod
    def getapply_xpath():
        apply_xpath = config.get('jobdetail section', 'apply_button_xpath')
        return apply_xpath

    @staticmethod
    def get_direct_apply_xpath():
        directapply_xpath = config.get('jobdetail section', 'direct_apply_button_xpath')
        return directapply_xpath

    @staticmethod
    def get_db_details(value):
        conn_string = config.get('db details', 'conn_string')
        db = config.get('db details', 'db')
        collection = config.get('db details', 'collection')
        ignore_collection = config.get('db details', 'ignoreCollection')
        company_collection = config.get('db details', 'companyCollection')
        if value == 'url':
            return conn_string
        elif value == 'db':
            return db
        elif value == 'ignorelist':
            return ignore_collection
        elif value == 'collection':
            return collection
        elif value == 'company':
            return company_collection

    @staticmethod
    def get_title_keywords(department):
        qatitles = config.get('jobsearch section', 'qa_titles')
        developertitles = config.get('jobsearch section', 'developer_titles')
        devopstitles = config.get('jobsearch section', 'devops_titles')
        interntitles = config.get('jobsearch section', 'intern_titles')
        if department == 'qa':
            return qatitles
        elif department == 'developer':
            return developertitles
        elif department == 'devops':
            return devopstitles
        elif department == 'intern':
            return interntitles
