import requests
import urllib
from bs4 import BeautifulSoup

# Configurations
DEFAULT_URL = "https://zbmath.org"


class ZbMath:
    """
    zbMath website API wrapper.
    """

    def run_query(self, search_term):
        """
        Search for a specific term.
        :param search_term: Term to search for, in plaintext without URL encoding.
        :return: A list of results.
        """
        r = requests.get(DEFAULT_URL + '?f=' + urllib.parse.quote_plus(search_term))
        html = BeautifulSoup(r.text, 'html.parser')
        result = []
        for article in html.select('.content-result .list article'):
            item = {
                'title': article.select('div.title a')[0].text.strip(),
                'link': DEFAULT_URL + article.select('div.title a')[0].get('href'),
                'authors': []
            }
            for author_div in article.select('div.author a'):
                item['authors'].append(author_div.text)
            result.append(item)
        return result
