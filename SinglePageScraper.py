# imports for de functie SinglePageScraper
import requests
from bs4 import BeautifulSoup
from bs4 import Comment



# The function scrapes a specific url and checks if there is a match with the defined keywords
def SinglePageScraper(url, keywords, string_finding_part_1,string_finding_part_2):

    result = requests.get(url)

    # check for status HTTP status code
    if result.status_code == 200:
        c = result.content

        # get comments
        soup = BeautifulSoup(c, 'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))

        positive_keywords = []


        for comment in comments:

            for keyword in keywords:
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
            print(string_finding_part_1 + url + string_finding_part_2 + string_positive_keywords)
        else:
            print("NO MATCHES")

    else:
        print("HTTP request failed, HTTP reponse status code: " + result.status_code)


def setURL():

    print("nog even iets voor bouwen")

#
# # Inlezen initiele configuratie, wanneer er een fout optreedt wordt dit in de console weergegeven
# if not loadIniConfig():
#     print("Config file read error")
#
# # Scrape page
# print(SinglePageScraper("https://dwg.nl", config["KEYWORDS"]))
