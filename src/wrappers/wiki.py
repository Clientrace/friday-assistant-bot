import json
import requests


class WikiQuery:
  """
  Wikipedia Querying Module
  """

  def __init__(self):
    self.HOST_URL = 'http://en.wikipedia.org/w/api.php'
    self.ARTICLE_URL = 'http://en.wikipedia.org'



  def query_by_title(self, title):
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

    response = requests.get(self.HOST_URL, params=params)
    return response.json()


  def query_by_pageid(self, pageID, sentenceNum):
    params = {
      'action' : 'query',
      'prop' : 'extracts|revisions',
      'rvprop' : 'content',
      'pageids' : pageID,
      'format' : 'json',
      'formatversion' : 2,
      'redirects' : True,
      'explaintext' : '',
      'exsentences' : sentenceNum
    }
    response = requests.get(self.HOST_URL, params=params)
    return response.json()


  @staticmethod
  def _normalize(msg):
    ret = ''
    for words in msg.split(' '):
      ret += words.capitalize() + ' '
    return ret

  @staticmethod
  def _query_transform(query):
    q = json.load(open('src/wrappers/q.json').read())
    for pharse in q['ignore_phrases']:
      query = query.replace(pharse,'')
    return query

  def get_description(self, pageids):
    concatPageIds = pageids[0]
    for pid in pageids[1:]:
      concatPageIds += '|' + pid
    params = {
      'action' : 'query',
      'prop' : 'categories|description',
      'clcategories' : 'Category:All article disambiguation pages|Category:All disambiguation pages',
      'format' : 'json',
      'pageids' : concatPageIds
    }
    response = requests.get(self.HOST_URL, params=params)
    return response.json()


  def search(self, query, resultsNum=10, suggest=False):
    params = {
      'action' : 'query',
      'format' : 'json',
      'list' : 'search',
      'prop' : 'description|categories',
      'srprop' : '',
      'srlimit' : resultsNum,
      'srsearch' : query,
      'srsort' : 'relevance'
    }
    if( suggest ):
      params['srinfo'] = 'suggestion'

    response = requests.get(self.HOST_URL, params=params)
    return response.json()

