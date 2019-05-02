from GrapyClasses import *


# Get init config
initConfig = IniConfig()
crawler_findings = []


if(initConfig.status != "FAILED"):

    # initialize SinglePageScraper variables
    singePageScraper = SinglePageScraper(initConfig.keywords, initConfig.string_finding_part1, initConfig.string_finding_part2)
    crawler = Crawler()
    export = Export()
    singlePageScraperFinding = None


    ## Main menu Grappy
    def print_menu():  ## Your menu design here
        print(30 * "-", "MENU", 30 * "-")
        print("1. Set URL")
        print("2. Show URL")
        print("3. Add a new keyword")
        print("4. Show keywords")
        print("5. Delete keyword")
        print("6. Run SinglePageScraper")
        print("7. Export singlePageScraper finding")
        print("8. Run Crawler")
        print("9. Export crawler findings")
        print("10. Exit")
        print(67 * "-")


    loop = True

    while loop:  ## While loop which will keep going until loop = False
        print_menu()  ## Displays menu
        choice = int(input("Enter your choice [1-5]: "))

        if choice == 1:
            initConfig.setUrl()
        elif choice == 2:
            initConfig.showURL()
        elif choice == 3:
            initConfig.addKeyword()
        elif choice == 4:
            singePageScraper.showKeywords()
        elif choice == 5:
            initConfig.deleteKeyword()
        elif choice == 6:
            singlePageScraperFinding = singePageScraper.runSinglePageScraper(initConfig.url)
        elif choice == 7:
            if singlePageScraperFinding == None:
                print("There a no findings to export, first run the SinglePageScraper")
            else:
                singePageScraper.writeToFileExchange(initConfig.exchange_path, initConfig.exchange_name, singlePageScraperFinding)
                # delete finding after export
                singlePageScraperFinding = None
        elif choice == 8:
            crawler_findings = crawler.runCrawler(initConfig.url, initConfig)
        elif choice == 9:
            export.createReport(crawler_findings)
        elif choice == 10:
            print ("so long, gay boy")
            ## You can add your code or functions here
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")

else:
     print("Error during retrieving config file")
