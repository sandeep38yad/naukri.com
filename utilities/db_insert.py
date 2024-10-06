from pymongo import MongoClient
from utilities.customLogger import LogGen
from datetime import datetime
from utilities.readProperties import ReadConfig

client = MongoClient(ReadConfig.get_db_details('url'))
db = client[ReadConfig.get_db_details('db')]
collection = db[ReadConfig.get_db_details('collection')]
company_collection = db[ReadConfig.get_db_details('company')]
logger = LogGen.loggen('naukri_automation')
class insertDB:
    success = 0
    def insert_company(company):
        if not company_collection.find_one({'company': company}):
            company_collection.insert_one({'company': company})

    def check_availibility(c, query):
        try:
            if c == "main":
                if collection.find_one(query):
                    return True
            elif c == "company":
                if company_collection.find_one(query):
                    return True
            return False
        except Exception as e:
            print(f'Error in check_availibility: {str(e)}')

    def insert_document(c, doc):
        try:
            if c == "main":
                collection.insert_one(doc)
            elif c == "company":
                company_collection.insert_one(doc)
        except Exception as e:
            print(f'Error in insert_document : {str(e)}')

    @staticmethod
    def start_insert(doclist):
        try:
            # print(f'Total {len(doclist)} inserting...')
            file_data_list = []
            failed_to_insert = []
            for doc in doclist:
                try:
                    insertDB.insert_company(doc['company'])
                    if not collection.find_one(doc):
                        doc['time'] = datetime.now()
                        doc['portal'] = 'naukri'
                        file_data_list.append(doc)
                        collection.insert_one(doc)
                        insertDB.success += 1
                        print(f'{doc["company"]} inserted successfully')
                except Exception as e:
                    failed_to_insert.append(doc)
                    print(f'Error in start_insert: {str(e)}')
                    logger.error(f'Error in start_insert: {str(e)}')

            print(f'{insertDB.success} inserted in DB')
            if failed_to_insert:
                print(f'Retrying to insert {len(doclist) - insertDB.success} ')
                insertDB.start_insert(failed_to_insert)
            else:
                print(f'All Inserted in DB')
                return True
            # if file_data_list:
            #     collection.insert_many(file_data_list)
            #     return True
        except Exception as e:
            print(f'Error in start_insert {str(e)}')
            logger.error(f'Error in start_insert: {str(e)}')
            return False


