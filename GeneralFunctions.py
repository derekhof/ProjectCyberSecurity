# import voor de config lader
import json

# Functions reads a config file and returns object or string
def loadIniConfig():

    try:
        # read config file
        with open('config.json', 'r') as f:
            config = json.load(f)

            return config
    except:

        return "FAILED"

# Functions prints keywords
def showKeywords(*keywords):
    for keyword in keywords:
        print("\n" + keyword)


