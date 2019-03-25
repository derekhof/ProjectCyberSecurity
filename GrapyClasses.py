# imports for de functie SinglePageScraper
import requests
from GeneralFunctions import *
from bs4 import BeautifulSoup
from bs4 import Comment


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
                        if keyword in comment:

                            # add positive match to results
                            positive_keywords.append(keyword)

                            # temp test
                            # print(comment)
                            # print("===========")
                            # comment.extract()


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
                    print( self.string_finding_part1 + self.url +  self.string_finding_part2 + string_positive_keywords)
                else:
                    print("NO MATCHES")

            else:
                print("HTTP request failed, HTTP reponse status code: " + result.status_code)

        except:
            print("The URL is not valid or not set! set a valid URL. Use the following structure: http(s)://xxxx.xx ")

    def showURL(self):
        return print(self.url)




class loadIniConfig:

    def __init__(self):
        try:
            # read config file
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.string_finding_part1 = config["DEFAULT_FINDING_STRING_PART_1"]
                self.string_finding_part2 = config["DEFAULT_FINDING_STRING_PART_2"]
                self.keywords = config["KEYWORDS"]
                self.status = "SUCCEED"
        except:

            self.status = "FAILED"




