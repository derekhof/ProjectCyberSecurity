# import the package
import defectdojo
import datetime

import random
import json
import os

class defectDojoParams:

    def __init__(self):
        self.host = None
        self.api_key = None
        self.user = None
        self.user_id = None
        self.dd = None

class dejectDojoTestResult:

    def __init__(self):
        self.findings = None
        self.name = None
        self.datetime = None


    def importJson(self, crawler_results):
        self.name = crawler_results["NAME"]
        self.datetime = crawler_results["DATETIME"]
        self.findings = crawler_results["FINDING"]



class defectDojoInterface:

    def __init__(self, connection_params):
        self.params = connection_params
        self.product_id = None
        self.engagament_id = None

    # This function initiates a connection with the defect dojo engine based on the params
    def setupConnection(self):
        try:
            # instantiate the DefectDojo api wrapper
            self.dd = defectdojo.DefectDojoAPI(self.params.host, self.params.api_key, self.params.user, debug=False, verify_ssl=False)
            return True

        except:
            # return false when connection failed
            return False


    def getExistingProducts(self):

        # check if there is a connection
        if self.dd != None:

            products = self.dd.list_products()
            return products.data["objects"]

    def checkProductID(self, product_id):

         product = self.dd.get_product(product_id)
         if product.message == "Object id does not exist.":
             return False

         self.product_id = product_id


         return True

    def getProductName(self, product_id):
        product = self.dd.get_product(product_id)
        json_str = json.loads(product.data_json())
        return json_str["name"]

    def getExistingEngagements(self, product_id, product_name):

        # check if there is a connection
        if self.dd != None:
            engagement = self.dd.list_engagements(product_in=product_id, name_contains="Intial " + product_name + " Engagement")
            return engagement.data["objects"]


    def checkEngagementID(self, engagement_id):

         engagement = self.dd.get_engagement(engagement_id)
         if engagement.message == "Object id does not exist.":
             return False

         self.engagament_id = engagement_id

         print(self.engagament_id)

         return True


    def getEngagementName(self, engagement_id):
        product = self.dd.get_engagement(engagement_id)
        json_str = json.loads(product.data_json())
        return json_str["name"]

    def exportToDefectDojo(self, testResult):
        print(testResult.name)

        # Create Test
        user_id = 1

        test_type = 30  # Web Test
        environment = 3  # Production environment
        test = self.dd.create_test(self.engagament_id, test_type, environment,
                              testResult.datetime, testResult.datetime)
        test_id = test.id()

        print("test id: " + str(test_id))

        for finding in testResult.findings:
            print(finding)

            self.dd.create_finding(str(finding["FINDING"]), str(finding["KEYWORDS"]), "Low", 1, "2019-05-16",self.product_id, self.engagament_id, test_id, user_id, "duwnwuwef", "wfefe", "No", "uhdwue")








class grappyCrawlerInterface:

    def __init__(self):
        self.testResult = dejectDojoTestResult()
        self.status = False

    def getExistingCrawlerResults(self):

        json_files = []
        dir = "findings"

        for file in os.listdir(dir):
            if file.endswith(".json"):
                json_files.append(dir + "/" + file)

        return json_files

    def getTestResult(self, path_test_result_json_file):

        try:
            # read config file
            with open(path_test_result_json_file, 'r') as f:
                test_result_json = json.load(f)
                self.status = True

            self.testResult.importJson(test_result_json)


        except:
            self.status = False

        return  self.testResult







