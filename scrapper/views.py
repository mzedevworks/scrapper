from pyramid.view import view_config
from scrapper.lib.scrape import Scrape
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    context = {}
    if 'url' in request.params:
        try:
            url = request.params['url']
            urlopen(url)
            scrape = Scrape(url)
            toc = scrape.start()
            if toc:
                redirect_url=request.route_url('results', _query={'html': toc})
                return HTTPFound(location=redirect_url)
            else:
                context.update({"error": "The wiki page you entered doesnt have a table of contents"})
        except (URLError, HTTPError) as e:
            context.update({"error": "Invalid wiki url entered. Try again"})
    return context

@view_config(route_name='results', renderer='templates/results.jinja2')
def results(request):
    context = {}
    if 'html' in request.params:
        html = request.params['html']
        context.update({"results": html})
    return context
