from bottle import template
import json
import os

JSON_FOLDER = '.\\data\\'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871", "2993", "305"]


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


data = {
    "result": []
}


def load_data():
    show_jsons = os.listdir(JSON_FOLDER)
    print(show_jsons)
    for show in show_jsons:
        show_id = show.split('.')[0]
        with open(JSON_FOLDER + show, encoding='utf-8') as f:
            show_info = json.load(f)
            data["result"].append(show_info)
