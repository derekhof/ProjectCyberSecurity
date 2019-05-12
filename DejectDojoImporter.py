# import the package
import defectdojo
import datetime
import random


# setup DefectDojo connection information
host = 'http://192.168.178.23:8000'
api_key = '5de86e2ee9d78f16de3b1b8029c1dff903453a46'
user = 'root'
user_id = 1


# instantiate the DefectDojo api wrapper
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True,verify_ssl=False)

# Create a product
# Search and see if product exists so that we don't create multiple product entries
product_name = "The DWG demo product"
products = dd.list_products(name_contains=product_name)
product_id = None

if products.count() > 0:
    for product in products.data["objects"]:
        product_id = product['id']
else:
    # Create a product
    prod_type = 1 #1 - Research and Development, product type
    product = dd.create_product(product_name, "This is a detailed product description.", prod_type)

    # Get the product id
    product_id = product.id()
    print("Product successfully created with an id: " + str(product_id))


# Retrieve the newly created product
product = dd.get_product(product_id)

#product_name = "Acme API Finding Demo"
engagement = dd.list_engagements(product_in=product_id, name_contains="Intial " + product_name + " Engagement")
engagement_id = None


start_date = datetime.datetime.now()
end_date = start_date + datetime.timedelta(days= random.randint(2,8))

if engagement.count() > 0:
    for engagement in engagement.data["objects"]:
        engagement_id = engagement['id']
else:
    # Create an engagement
    print ("Creating engagement: " + "Intial " + product_name + " Engagement")
    engagement = dd.create_engagement("Intial " + product_name + " Engagement", product_id, user_id,
    "In Progress", start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
    engagement_id = engagement.id()


print("Creating the test")
# Create Test
test_type = 5 #Web Test
environment = 3 #Production environment
test = dd.create_test(engagement_id, test_type, environment,
start_date.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d"))
test_id = test.id()

print("Creating the finding")
build = "Jenkins-" + str(random.randint(100,999))

# Create Finding
finding = dd.create_finding("Crawler test", "Test finding", "Low", 1,start_date.strftime("%Y-%m-%d"), product_id, engagement_id, test_id,user_id, "duwnwuwef", "wfefe","No","uhdwue")



print("Listing the new findings for this build")