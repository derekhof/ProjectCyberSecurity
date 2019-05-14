from  DefectDojoClasses import *

# Set connection params for Deject Dojo (temp -> function for reading it from config file)
connection_params = defectDojoParams()
connection_params.host = 'http://192.168.241.129:8000'
connection_params.api_key = '5de86e2ee9d78f16de3b1b8029c1dff903453a46'
connection_params.user = 'root'
connection_params.user_id = 1

# Initialize the connection
ddInterface = defectDojoInterface(connection_params)

# Function prints all the existing products
def printProducts(products):
    print("Defect Dojo Products: ")
    for product in products:
        print(product['name'] + " - " + "(ID = " + str(product['id']) + ")")
        print("******************")

def selectAndValidatePoductID():

    try:
        product_id = int(input("Product ID = ?"))
        if ddInterface.checkProductID(product_id):
            print("selected product: " + ddInterface.getProductName(product_id))
            return product_id
        else:
            print("Product ID does not exist")
            return None
    except:
        print("Only use numbers are allowed")



## Main menu Grappy
def print_menu(oonnection, product_id):  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. Initiate connection with Defect Dojo")
    if connection:
        print("2. Show existing product")
        print("3. Select a product")

        if product_id != None:
            print("4. Show engagements")

    print("10. Exit")
    print(67 * "-")

# init loop state
loop = True
connection = False
product_id = None

while loop:  ## While loop which will keep going until loop = False
    print_menu(connection, product_id)  ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))

    if choice == 1:
        connection = ddInterface.setupConnection()
    elif choice == 2:
        printProducts(ddInterface.getExistingProducts())
    elif choice == 3:
        product_id = selectAndValidatePoductID()
    elif choice == 4:
        engagement_id = ddInterface.getExistingEngagements(product_id, ddInterface.getProductName(product_id))
    elif choice == 10:
        loop = False



