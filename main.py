import os
from typing import List, Any

from bottle import get, post, redirect, request, route, run, static_file, template, error, response
import utils
import json

p = os.path.abspath(os.getcwd())

# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/', method="GET")
def index():
    sectionTemplate = os.path.join(p, "templates", "home.tpl")
    return template(os.path.join(p, "pages", "index.html"), version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse', method="GET")
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=utils.data["result"])


@route('/search', method="GET")
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/ajax/show/<show_id:int>', method='GET')
def show(show_id):
    show = utils.get_show_by_id(show_id)
    if any(show):
        sectionTemplate = "./templates/show.tpl"
        return template(sectionTemplate, result=show)
    else:
        return False


@route('/show/<show_id:int>', method="GET")
def return_show_page(show_id):
    show = utils.get_show_by_id(show_id)
    if any(show):
        sectionTemplate = "./templates/show.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=show)
    else:
        return False

@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template(sectionTemplate)


def main():
    utils.load_data()
    run(host='localhost', port=os.environ.get('PORT', 5000))


if __name__ == "__main__":
    main()
