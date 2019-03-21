# import voor de config lader
import json

# Functions reads a config file and stores values in global var
def loadIniConfig():

    try:
        # read config file
        with open('config.json', 'r') as f:
            config = json.load(f)

            return config
    except:

        return "FAILED"


def showKeywords(*keywords):
    for keyword in keywords:
        print("\n" + keyword)


