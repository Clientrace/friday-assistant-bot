import json
import requests


class WikiQuery:
  """
  Wikipedia Querying Module
  """

  def __init__(self):
    self.HOST_URL = 'http://en.wikipedia.org/w/api.php'
    self.ARTICLE_URL = 'http://en.wikipedia.org'


  @staticmethod
  def _query(url, title):
    params = {
      'action' : 'query',
      'prop' : 'extracts',
      'titles' : title,
      'format' : 'json',
      'formatversion' : 2,
      'redirects' : True,
      'explaintext' : '',
      'exsentences' : 15
    }

    response = requests.get(url, params=params)
    return response.json()


  def get_content(self, title):
    qresp = WikiQuery._query(self.HOST_URL, title)
    return qresp['query']['pages'][0]['extract']