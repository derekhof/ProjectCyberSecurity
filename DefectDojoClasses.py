# import the package
import defectdojo
import datetime
import random
import json


class defectDojoParams:

    def __init__(self):
        self.host = None
        self.api_key = None
        self.user = None
        self.user_id = None
        self.dd = None


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

         return True

    def getProductName(self, product_id):
        product = self.dd.get_product(product_id)
        json_str = json.loads(product.data_json())
        return json_str["name"]

    def getExistingEngagements(self, product_id, product_name):

        engagement = self.dd.list_engagements(product_in=product_id, name_contains="Intial " + product_name + " Engagement")

        if engagement.count() > 0:
            for engagement in engagement.data["objects"]:
                print(engagement['name'] + " - ID = " + str(engagement['id']))








