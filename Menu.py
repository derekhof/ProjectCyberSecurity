

# py -m pip install
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from SinglePageScraper import *
from GeneralFunctions import *

## Global variables
config = 0

## get init config
config = loadIniConfig()
if(config != "FAILED"):



    # Create the menu
    menu = ConsoleMenu("Grappy - Web Scraper", "Select a function!")

    # Create some items

    # Submenu items for the Console menu: SingeScraper Functionality
    function_item_setURL = FunctionItem("Set URL", setURL)
    function_item_run_singlepagescraper = FunctionItem("Run", SinglePageScraper, ["https://dwg.nl", config["KEYWORDS"], config["DEFAULT_FINDING_STRING_PART_1"], config["DEFAULT_FINDING_STRING_PART_2"]])

    # A consolse menu for for SingeScraper Functionality
    console_menu_singlePageScraper = ConsoleMenu("-- Singe Page Scraper --")


    # a submenu item for the main menu singe page scraper
    submenu_items_singlePageScraper = SubmenuItem("Single Page Scraper", console_menu_singlePageScraper, menu = menu)


    # A FunctionItem runs a Python function when selected
    function_item_showKeywords = FunctionItem("Show all keywords", showKeywords, config["KEYWORDS"])

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command",  "touch hello.txt")



    # Once we're done creating them, we just add the items to the menu
    menu.append_item(submenu_items_singlePageScraper)
    menu.append_item(function_item_showKeywords)
    menu.append_item(command_item)


    #Submenu SinglePageScraper
    console_menu_singlePageScraper.append_item(function_item_setURL)
    console_menu_singlePageScraper.append_item(function_item_run_singlepagescraper)
    console_menu_singlePageScraper.append_item(function_item_showKeywords)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()


else:
    print("Error during retrieving config file")