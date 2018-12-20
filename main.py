import os
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


@get('/')
def index():
    sectionTemplate = os.path.join(p, "templates", "home.tpl")
    return template(os.path.join(p, "pages", "index.html"), version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData={})


@get('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    print(utils.data["result"])
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=utils.data["result"])


@route('/search', method="GET")
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@post('/search')
def return_search_results():
    query = request.forms.get('q')
    # match = utils.find_episodes(query)
    match = [{"text": "THIS IS AN EPISODE", "showid": 7, "episodeid": 19}]
    sectionTemplate = "./templates/search_result.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={},
                    results=match, query=query)


@get('/ajax/show/<show_id:int>')
def show(show_id):
    show = utils.get_show_by_id(show_id)
    if any(show):
        return template("./templates/show.tpl", result=show)
    else:
        response.status = 404
        return template("./templates/404.tpl")


@get('/show/<show_id:int>')
def return_show_page(show_id):
    show = utils.get_show_by_id(show_id)
    if any(show):
        sectionTemplate = "./templates/show.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                        sectionData=show)
    else:
        response.status = 404
        sectionTemplate = "./templates/404.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                        sectionData={})


@get('/ajax/show/<show_id:int>/episode/<episode_id:int>')
def episode(show_id, episode_id):
    episode = utils.get_episode_by_id(show_id, episode_id)
    if any(episode):
        return template("./templates/episode.tpl", result=episode)
    else:
        response.status = 404
        return template("./templates/404.tpl")


@get('/show/<show_id:int>/episode/<episode_id:int>')
def return_episode_page(show_id, episode_id):
    episode = utils.get_episode_by_id(show_id, episode_id)
    if any(episode):
        sectionTemplate = "./templates/episode.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                        sectionData=episode)
    else:
        response.status = 404
        sectionTemplate = "./templates/404.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                        sectionData={})


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template(sectionTemplate)


def main():
    utils.load_data()
    run(host='localhost', port=os.environ.get('PORT', 5000))


if __name__ == "__main__":
    main()
