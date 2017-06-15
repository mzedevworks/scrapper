"""
#   author - Musavengana Zirebwa
#   email - musaz01@gmail.com
#   created - 2017/06/14 9:53 PM
#   version - 1.0.0
#   project - siyavula

:description: Use this class to load a URL.
"""
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

class Loader(object):
    def load(self, url):
        """
        load(url) will automatically be called by the scraper.
        :param url: Url to load
        :return: html from the given url
        """
        html = ''
        try:
            html = self.loader(url)
        except:
            return ''
        return html

    def loader(self, url):
        """
        :param url: URL of the location to scrape
        :return: If successful, it returns some html. Else it will return an nothing
        """
        html = ''
        try:
            res = urlopen(url)
            html = res.read()
        except (URLError, HTTPError) as e:
            print(e)
            return html

        return html
