"""
#   author - Musavengana Zirebwa
#   email - musaz01@gmail.com
#   created - 2017/06/14 9:53 PM
#   version - 1.0.0
#   project - siyavula

:description:
This is the class used to scrape a given wikipedia url
"""
from scrapper.lib.scrape_factory import ScrapeFactory


class Scrape:
    def __init__(self, url):
        self.url = url

    def start(self):
        """
        Scrape the appropriate source and return the html.

        :return html table of contents:
        """
        try:
            factory = ScrapeFactory()

            loader = factory.load()
            parser = factory.parse()

            html = loader.load(self.url)
            table_of_contents_html = parser.parse(html)
            return table_of_contents_html
        except:
            return {"error": "Error while scrapping html enter another url"}
