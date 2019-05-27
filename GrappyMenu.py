from GrapyClasses import *
from pyfiglet import Figlet
import sys




# Get init config
initConfig = IniConfig()
crawler_findings = []

if(initConfig.status != "FAILED"):

    # initialize SinglePageScraper variables
    singePageScraper = SinglePageScraper(initConfig.keywords, initConfig.string_finding_part1, initConfig.string_finding_part2)
    crawler = Crawler()
    crawlerResult = CrawlerResult()
    singlePageScraperFinding = None
if (sys.argv[1] == 'auto'):
    crawler_findings = crawler.runCrawler(initConfig.url, initConfig)
    crawlerResult.defineTestName()
    crawlerResult.createReport(crawler_findings)
    crawlerResult.writeToFileExchange(initConfig.url)
    # delete results
    crawlerResult = None
    exit(1)


    ## Main menu Grappy
    def print_menu():  ## Your menu design here

        f = Figlet(font='isometric2')
        print(f.renderText('Grappy'))
        print(30 * "-", "MENU", 30 * "-")
        print("\033[31m" + "1. Set URL")
        print("\033[31m" + "2. Show URL")
        print("\033[31m" + "3. Show keywords")
        print("\033[31m" + "4. Add a new keyword")
        print("\033[31m" + "5. Delete keyword")
        print("\033[31m" + "6. Run SinglePageScraper")
        print("\033[31m" + "7. Export singlePageScraper finding")
        print("\033[31m" + "8. Run Crawler")
        print("\033[31m" + "9. Export crawler findings")
        print("\033[31m" + "10.Exit\n")
        print(67 * "\033[31m-")


    loop = True

    while loop:  ## While loop which will keep going until loop = False
        print_menu()  ## Displays menu
        choice = int(input("\033[37mEnter your choice: "))

        if choice == 1:
            initConfig.setUrl()
        elif choice == 2:
            initConfig.showURL()
        elif choice == 3:
            initConfig.showKeywords()
        elif choice == 4:
            initConfig.addKeyword()
        elif choice == 5:
            initConfig.showKeywords()
            print(" ")
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

            if crawlerResult == None:
                print("There a no findings to export, first run the Crawler")
            else:
                crawlerResult.defineTestName()
                crawlerResult.createReport(crawler_findings)
                crawlerResult.writeToFileExchange(initConfig.url)
                # delete results
                crawlerResult = None

        elif choice == 10:
            print ("So long, and thanks for the fish!")
            ## You can add your code or functions here
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")

else:
     print("Error during retrieving config file")
