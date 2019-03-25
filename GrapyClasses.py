# imports for de functie SinglePageScraper
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import json


class SinglePageScraper:

    def __init__(self, keywords, string_finding_part_1, string_finding_part_2):
        self.keywords = keywords
        self.string_finding_part1 = string_finding_part_1
        self.string_finding_part2 = string_finding_part_2
        self.url = None



    def setUrl(self):
        self.url = input("Set URL:")


    def showKeywords(self):
        for keyword in self.keywords:
            print("\n" + keyword)

    # The function scrapes a specific url and checks if there is a match with the defined keywords
    def runSinglePageScraper(self):

        try:
            result = requests.get(self.url)

            # check for status HTTP status code
            if result.status_code == 200:
                c = result.content

                # get comments
                soup = BeautifulSoup(c, 'html.parser')
                comments = soup.find_all(string=lambda text: isinstance(text, Comment))

                positive_keywords = []


                for comment in comments:

                    for keyword in self.keywords:

                        # temp test
                        print(comment)
                        print("===========")
                        comment.extract()
                        if keyword in comment:

                            # add positive match to results
                            positive_keywords.append(keyword)


                # remove duplicatie keyword matches
                positive_keywords = list(set(positive_keywords))

                # Create string with findings
                string_positive_keywords = ""
                counter = 0
                for positive_keyword in positive_keywords:
                    if counter == 0:
                        string_positive_keywords = string_positive_keywords + positive_keyword
                    else:
                        string_positive_keywords = string_positive_keywords + ", " + positive_keyword

                    counter = counter + 1

                # print(string_finding_part_1)
                # print(string_finding_part_2)
                # print(url)
                # print(string_positive_keywords)


                # return results
                if counter > 0:
                    self.finding = Finding(self.url, self.keywords)
                    print( self.string_finding_part1 + self.url +  self.string_finding_part2 + string_positive_keywords)

                else:
                    print("NO MATCHES")

            else:
                print("HTTP request failed, HTTP reponse status code: " + result.status_code)

        except:
            print("The URL is not valid or not set! set a valid URL. Use the following structure: http(s)://xxxx.xx ")

    def showURL(self):
        return print(self.url)

    def writeToFileExchange(self, path, fileName):

        try:

            filePathNameWExt = './' + path + '/' + fileName + '.json'
            with open(filePathNameWExt, 'w') as fp:
                json.dump(self.finding.resultToDict(), fp)

                print("Finding are succesfully exported")

        except:
            print("There are no findings")





class Finding:
    def __init__(self, url, keywords):
        self.url = url
        self.keywords = keywords
        self.dict = None


    def resultToDict(self):
        self.dict = {}
        self.dict["URL"] = self.url
        self.dict['Keywords'] = self.keywords

        return self.dict




class IniConfig:

    def __init__(self):
        try:
            # read config file
            with open('config.json', 'r') as f:
                self.config = json.load(f)
                self.exchange_path = self.config["FILE_EXCHANGE_PATH"]
                self.exchange_name = self.config["FILE_EXCHANGE_NAME"]
                self.string_finding_part1 = self.config["DEFAULT_FINDING_STRING_PART_1"]
                self.string_finding_part2 = self.config["DEFAULT_FINDING_STRING_PART_2"]
                self.keywords = self.config["KEYWORDS"]
                self.status = "SUCCEED"
        except:

            self.status = "FAILED"


    def addKeyword(self):

        doubleKeyword = False
        newKeyword = input("Add a new keyword: ")

        # Check if keyword already exist
        for keyword in self.keywords:
            if keyword == newKeyword:
                print("Keyword already exists")
                doubleKeyword = True

        # only add keyword if it is does already exists
        if doubleKeyword == False:
                self.keywords.append(newKeyword)
                self.config["KEYWORDS"] = self.keywords

                with open('config.json', 'w') as f:
                    json.dump(self.config, f)



    def deleteKeyword(self):

        KeywordExists = False
        deleteKeyword = input("Which keyword do you want to delete:")

        # Check if keyword already exist
        for keyword in self.keywords:
            if keyword == deleteKeyword:

                KeywordExists = True

        # only add keyword if it is does already exists
        if KeywordExists == True:
                self.keywords.remove(deleteKeyword)
                self.config["KEYWORDS"] = self.keywords

                with open('config.json', 'w') as f:
                    json.dump(self.config, f)

                print("Keyword deleted")

        else:
            print("Keyword does not exists")
