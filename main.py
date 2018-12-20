import os
from bottle import get, post, redirect, request, route, run, static_file, template, error, response
import utils
import json


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


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=utils.data["result"])


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/show/<show_id:int>')
def show(show_id):
    show_as_list = [show for show in utils.data["result"] if show['id'] == show_id]
    if any(show_as_list):
        show = show_as_list[0]
        sectionTemplate = "./templates/show.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                        sectionData=show)
    else:
        response.status = 404
        return False


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


def main():
    utils.load_data()
    run(host='localhost', port=os.environ.get('PORT', 5000))


if __name__ == "__main__":
    main()
