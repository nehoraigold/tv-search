from bottle import template
import json
import os

JSON_FOLDER = '.\\data\\'
AVAILABLE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871", "2993", "305"]


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def get_show_by_id(show_id):
    show_as_list = [show for show in data["result"] if show['id'] == show_id]
    return show_as_list[0] if any(show_as_list) else {}


def get_episode_by_id(show_id, episode_id):
    show = get_show_by_id(show_id)
    if show:
        episode_as_list = [episode for episode in show["_embedded"]["episodes"] if episode["id"] == episode_id]
        return episode_as_list[0] if any(episode_as_list) else {}
    else:
        return {}


def load_data():
    return [json.loads(getJsonFromFile(show)) for show in AVAILABLE_SHOWS]


data = {
    "result": load_data()
}
