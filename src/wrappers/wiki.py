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
      'exsentences' : 1
    }

    response = requests.get(url, params=params)
    return response.json()

  @staticmethod
  def _normalized(msg):
    ret = ''
    for words in msg.split(' '):
      ret += words.capitalize() + ' '
    return ret


  def get_content(self, title):
    title = WikiQuery._normalized(title)
    qresp = WikiQuery._query(self.HOST_URL, title)
    if( 'extract' in qresp ):
      return qresp['query']['pages'][0]['extract']
    else:
      return None