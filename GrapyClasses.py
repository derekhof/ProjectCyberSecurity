# imports for de functie SinglePageScraper
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
from bs4 import Comment
import datetime
import json, re
import os



from time import gmtime, strftime


class SinglePageScraper:

    def __init__(self, keywords, string_finding_part_1, string_finding_part_2):
        self.keywords = keywords
        self.string_finding_part1 = string_finding_part_1
        self.string_finding_part2 = string_finding_part_2


    # The function scrapes a specific url and checks if there is a match with the defined keywords
    def runSinglePageScraper(self, url):

        try:
            result = requests.get(url)

            # check for status HTTP status code
            if result.status_code == 200:
                c = result.content

                # get comments
                soup = BeautifulSoup(c, 'html.parser')
                comments = soup.find_all(string=lambda text: isinstance(text, Comment))

                positive_keywords = []

                for comment in comments:

                    for keyword in self.keywords:
                        #
                        # # temp test
                        # print(comment)
                        # print("===========")
                        # comment.extract()
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

                # return results
                if counter > 0:
                    self.finding = Finding(url, string_positive_keywords)
                    print(self.string_finding_part1 + url + self.string_finding_part2 + string_positive_keywords)

                    return self.finding

                else:
                    print(self.string_finding_part1 + url + " NO MATCHES")

            else:
                print("HTTP request failed, HTTP reponse status code: " + str(result.status_code))

        except:
                print("The URL is not valid or not set! set a valid URL. Use the following structure: http(s)://xxxx.xx ")


    # Function writes a single page scraper finding to a json file. The filename and filepath can be changed in the config.json file
    # Function first retreives existing exported findings. If the file does not contain findings, a new findings json array will me created.

    def writeToFileExchange(self, path, fileName, singlePageScraperFinding):


        filePathNameWExt = './' + path + '/' + fileName + '.json'

        # retrieve existing test results
        try:
            # read config file
            with open(filePathNameWExt, 'r') as f:

            # deserialize object and check is if the file contains json objects
                try:
                    results = json.load(f)
                    fileIsEmpty = False

                except:
                    fileIsEmpty = True

                fileRetrieved = True
        except:

            fileRetrieved = False



        # check if file has successfully been retrieved
        if fileRetrieved:

            # check if the file is empty
            if fileIsEmpty:

                # create a new json array
                results = []


            # append new finding to json array
            results.append(singlePageScraperFinding.resultToJson())

            # write new results json array to file
            try:

                 with open(filePathNameWExt, 'w') as fp:

                     json.dump(results, fp)

                     print("Finding are succesfully exported")

            except:
                    print("Error during file write action")

        else:
                print("Error during file retrieve action")



# Configuration handler class
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
                self.url = self.config["DEFAULT_URL"]
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


    def setUrl(self):
            self.url = input("Set URL:")


    def showKeywords(self):
        if len(self.keywords) > 0:
            for keyword in self.keywords:
                print("|" + keyword + "|")
        else:
            print("No keywords registered")


    def showURL(self):
        return print("\033[37m" + "The following url is set:" + self.url)


class Crawler:

    def handleLocalLinks(self, url, link):
        if link != None:
            if link.startswith('/'):
                return ''.join([url, link])
            else:
                return link

    def getLinks(self, url):
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            body = soup.body

            links = [link.get('href') for link in body.find_all('a')]
            links = [self.handleLocalLinks(url, link) for link in links]
            return links

        except TypeError as e:
            print(e)
            print('Got a TypeError, probably got a None that we tried to iterate over')
            return []
        except IndexError as e:
            print(e)
            print('We probably did not find any useful links, returning empty list')
            return []
        except AttributeError as e:
            print(e)
            print('Likely got None for links, so we are throwing this')
            return []
        except Exception as e:
            print(str(e))
            # log this error
            return []

    def removeDuplicates(self, data):
        seen = set()
        seen_add = seen.add
        return [x for x in data if not (x in seen or seen_add(x))]

    def createFqdn(self, url, link):
        if link != None:
            if not link.startswith('http'):
                return '/'.join([url, link])
            else:
                return link

    def runCrawler(self, url, config):
        data = self.getLinks(url)
        if None in data:
            data.remove(None)
        data = self.removeDuplicates(data)
        data = [self.createFqdn(url, link) for link in data]

        # use singeplagescraper
        singlePageScraper = SinglePageScraper(config.keywords, config.string_finding_part1, config.string_finding_part2)

        findings = []

        for link in data:
            finding = singlePageScraper.runSinglePageScraper(link)

            if finding != None:
                findings.append(finding)

        return findings




####################################################
############ Findings handler class ################
####################################################

class Finding:
    def __init__(self, url, keywords):

        self.date_time = datetime.datetime.now()
        self.url = url
        self.keywords = keywords
        self.dict = None
        self.findings = []


    def resultToJson(self):
        self.json = {}
        self.json["KEYWORDS"] = self.keywords
        self.json["FINDING"] = self.url
        self.json["DATETIME"] = str(self.date_time)

        return self.json


class CrawlerResult:

    def __init__(self):
        self.findings = None
        self.test_name = None
        self.date_time = datetime.datetime.now()


    def defineTestName(self):
        self.test_name = input("Name of the test = ?")


    def createReport(self, findings):

        self.findings = findings

        finding_list = []
        for finding in self.findings:

            finding_list.append(finding.resultToJson())


        self.findings = findings
        self.json = {}
        self.json["NAME"] = self.test_name
        self.json["FINDING"] = finding_list
        self.json["DATETIME"] = str(self.date_time)

    def writeToFileExchange(self, url):
        try:
            filePathNameWExt = "findings/" + re.sub("[.:/(\W*(http)\W*||\W*(https)\W]", "", url) + str(strftime("-%Y%m%d%H%M")) + ".json"
            print(filePathNameWExt)
            with open(filePathNameWExt, 'w') as fp:
                json.dump(self.json, fp)
                print("Finding are succesfully exported")
        except FileNotFoundError:
            print("Catch all !!")







