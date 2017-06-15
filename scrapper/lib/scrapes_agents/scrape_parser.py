"""
#   author - Musavengana Zirebwa
#   email - musaz01@gmail.com
#   created - 2017/06/14 9:53 PM
#   version - 1.0.0
#   project - siyavula

:description: Use this class to parse some html.
"""
from bs4 import BeautifulSoup
class Parser():
    """
    Parse html
    """
    def parse(self, html):
        """
        Parse some html to return part of the page
        :param j_obj:
        :return:
        """
        try:
            soup = BeautifulSoup(html)
            toc = soup.find("div", {"id": "toc"})
            return toc
        except:
            return {"error": "Error while parsing html"}
