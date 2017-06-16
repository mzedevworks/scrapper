from pyramid.view import view_config
from pyramid.renderers import render
from pyramid.response import Response
from pyramid.i18n import TranslationString
from urllib.request import urlopen
from scrapper.lib.scrape import Scrape

@view_config(route_name='home', renderer='templates/home.jinja2')
def home( request ):
    context = {}

    if 'url' in request.params:
        try:
            url = request.params['url']

            if 'wikipedia' in url:
                urlopen(url)
                scrape = Scrape(url)
                toc = scrape.start()
                if toc:
                    variables = {'html': toc}
                    output = render("templates/results.jinja2", variables, request=request)
                    return Response(output)
                else:
                    context.update( {"error": TranslationString("The wiki page you entered "
                                                               "doesnt have a table of contents")} )
            else:
                context.update({"error": TranslationString("The url you entered is not a valid wikipedia url")})
        except:
            context.update( {"error": TranslationString("Invalid wikipedia url format entered. Try again. "
                                                        "Dont leave out the https:// or http://")} )
    return context
