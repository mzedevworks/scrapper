"""
#   author - Musavengana Zirebwa
#   email - musaz01@gmail.com
#   created - 2017/06/14 9:53 PM
#   version - 1.0.0
#   project - siyavula

:description:
This is the class used to scrape a given wikipedia url
"""
from scrapper.lib.scrapes_agents.scrape_loader import Loader
from scrapper.lib.scrapes_agents.scrape_parser import Parser


class ScrapeFactory(object):
    """
    This factory can be used to get an instance of the appropriate load, parse or write objects.
    Can be easily extended for multiple sources
    """
    def load(self):
        """
        Every scraper will have it's own

        :param source (int) the source of the scrape:
        :return: void
        """
        return Loader()

    def parse(self):
        """
        Return a parser depending on source and can be different return types.
        :param source:
        :return:
        """
        return Parser()





