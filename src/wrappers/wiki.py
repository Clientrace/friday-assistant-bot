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
      'exsentences' : 3
    }

    response = requests.get(url, params=params)
    return response.json()

  @staticmethod
  def _normalized(msg):
    ret = ''
    for words in msg.split(' '):
      ret += words.capitalize() + ' '
    return ret


  def search(self, query, resultsNum=10, suggest=False):
    params = {
      'action' : 'query',
      'format' : 'json',
      'list' : 'search',
      'srprop' : '',
      'srlimit' : resultsNum,
      'srsearch' : query
    }
    if( suggest ):
      params['srinfo'] = 'suggestion'

    response = requests.get(self.HOST_URL, params=params)
    return response.content

  def get_content(self, title):
    title = WikiQuery._normalized(title)
    qresp = WikiQuery._query(self.HOST_URL, title)
    print(qresp)
    if( 'extract' in qresp['query']['pages'][0] ):
      return qresp['query']['pages'][0]['extract']
    else:
      return None