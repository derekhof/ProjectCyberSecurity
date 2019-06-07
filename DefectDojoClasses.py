# import the package
import defectdojo
import json
import os

class DefectDojoParams:

    def __init__(self):
        self.host = None
        self.api_key = None
        self.user = None
        self.user_id = None
        self.environment = None
        self.test_type = None
        self.engagement_id = None
        self.product_id = None
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


# Configuration handler class
class IniConfig:

    def __init__(self):

        self. defectDojoParams = DefectDojoParams()
        try:
            # read server_config file
            with open('server_config.json', 'r') as f:
                self.server_config = json.load(f)
                self.defectDojoParams.host = self.server_config["HOST"]
                self.defectDojoParams.api_key = self.server_config["API_KEY"]
                self.defectDojoParams.user = self.server_config["USER"]
                self.defectDojoParams.user_id = self.server_config["USER_ID"]
                self.defectDojoParams.environment = self.server_config["ENVIRONMENT"]
                self.defectDojoParams.test_type = self.server_config["TEST_TYPE"]
                self.defectDojoParams.engagement_id = self.server_config["ENGAGEMENT_ID"]
                self.defectDojoParams.product_id = self.server_config["PRODUCT_ID"]
                self.status = "SUCCEED"
        except:

            self.status = "FAILED"


    def getDefectDojoParams(self):
        return self.defectDojoParams



class defectDojoInterface:

    def __init__(self, connection_params):
        self.params = connection_params


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

         self.params.product_id = product_id


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

         self.params.engagament_id = engagement_id

         print(self.params.engagament_id)

         return True


    def getEngagementName(self, engagement_id):
        product = self.dd.get_engagement(engagement_id)
        json_str = json.loads(product.data_json())
        return json_str["name"]

    def exportToDefectDojo(self, testResult):

        print("Name test results: " + testResult.name)

        test = self.dd.create_test(self.params.engagement_id, self.params.test_type, self.params.environment, testResult.datetime, testResult.datetime)
        test_id = test.id()

        print("Test id: " + str(test_id))

        for finding in testResult.findings:
            print(finding)

            self.dd.create_finding(str(finding["FINDING"]), str(finding["KEYWORDS"]), "Low", 1, "2019-05-27", self.params.product_id, self.params.engagement_id, test_id, self.params.user_id, "duwnwuwef", "wfefe", "No", "uhdwue")


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

        return self.testResult








