from  DefectDojoClasses import *
from pyfiglet import Figlet

# Set connection params for Deject Dojo (temp -> function for reading it from config file)
init_config = IniConfig()
connection_params = init_config.getDefectDojoParams()

# Initialize the connection
ddInterface = defectDojoInterface(connection_params)

# initialize crawler result object
gcInterface = grappyCrawlerInterface()

# Initialize Defect Dojo test result object
ddTestResult = dejectDojoTestResult()

# Function prints all the existing products
def printProducts(products):
    print("DefectDojo Products: ")
    for product in products:
        print(product['name'] + " - " + "(ID = " + str(product['id']) + ")")
        print("******************")

def printEngagements(engagements):
    print("Product engagements: ")
    for engagement in engagements:
        print(engagement['name'] + " - " + "(ID = " + str(engagement['id']) + ")")
        print("******************")

def printTestResults(test_results):
    index = 0
    print("Product engagements: ")
    for test_result in test_results:
        print(test_result + " - " + "(ID = " + str(index) + ")")
        print("******************")
        index  = index + 1

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
        return None

def selectAndValidateEngagementID():
    try:
        engagement_id = int(input("Engagement ID = ?"))
        if ddInterface.checkEngagementID(engagement_id):
            print("selected engagement: " + ddInterface.getEngagementName(engagement_id))
            return engagement_id
        else:
            print("Engagement ID does not exist")
            return None
    except:
        print("Only use numbers are allowed")
        return None


def selectAndValidateTestResultID(list_test_result_files):
    try:
        test_result_id = int(input("Test result ID = ?"))
        if test_result_id <= len(list_test_result_files):
            print("selected test results: " + list_test_result_files[test_result_id])
            return list_test_result_files[test_result_id]
        else:
            print("Test result ID does not exist")
            return None
    except:
        print("Only use numbers are allowed")
        return None

def exportTestResults():
    ddTestResult = gcInterface.getTestResult(path_test_result_json_file)

    if gcInterface.status:
        ddInterface.exportToDefectDojo(ddTestResult)




## Main menu Grappy
def print_menu(step):  ## Your menu design here
    f = Figlet(font='isometric2')
    print(f.renderText('Grappy'))
    print(30 * "-", "DEFECTDOJO IMPORTER CONFIGURATION MENU", 30 * "-")

    if step == 1:
        print("\033[31m" + "1. Initiate connection with Defect Dojo")
    elif step == 2:
        print("\033[31m" + "2. Show existing product")
        print("\033[31m" + "3. Select a product")
    elif step == 3:
        print("\033[31m" + "4. Show engagements")
        print("\033[31m" + "5. Select a engagement")
    elif step == 4:
        print("\033[31m" + "6. Show crawler test results")
        print("\033[31m" + "7. Select crawler test results")
    elif step == 5:
        print("\033[31m" + "8. Export test result to DefectDojo")

    print("\033[31m" + "9. Restart configuration")
    print("\033[31m" + "10.Exit")
    print(67 * "-")

# init loop state
loop = True

product_id = None
path_test_result_json_file = None
engagement_id = None
step = 1

while loop:  ## While loop which will keep going until loop = False
    print_menu(step)  ## Displays menu
    choice = int(input("\033[37mEnter your choice : "))

    if choice == 1 and step == 1:
        # initialize connection and go to step 2 if connection is succeeded
        if ddInterface.setupConnection():
            step = 2
    elif choice == 2 and step == 2:
        printProducts(ddInterface.getExistingProducts())
    elif choice == 3 and step == 2:
        # select a product and validate product id. If successfull to step 3
        product_id = selectAndValidatePoductID()
        if product_id != None:
            step = 3
    elif choice == 4 and step == 3:
        printEngagements(ddInterface.getExistingEngagements(product_id, ddInterface.getProductName(product_id)))
    elif choice == 5 and step == 3:
        # select a engagement and validate product id. If successfull to step 3
        engagement_id = selectAndValidateEngagementID()
        if engagement_id != None:
            step = 4
    elif choice == 6:
        printTestResults(gcInterface.getExistingCrawlerResults())
    elif choice == 7:
        path_test_result_json_file = selectAndValidateTestResultID(gcInterface.getExistingCrawlerResults())
        if path_test_result_json_file != None:
            step = 5
    elif choice == 8:
        exportTestResults()
    elif choice == 9:
        product_id = None
        engagement_id = None
        step = 1
    elif choice == 10:
        loop = False



