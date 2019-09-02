"""
Chatbot Search Functionality
"""

import json
import _uxy_core
from src.wrappers.wiki import WikiQuery
from _uxy_core.utility.api_wrappers.facebook import Facebook

wikiQuery = WikiQuery()

def _search(query):
  result = wikiQuery.search(query, suggest=True)
  if( len(result['query']['search']) > 0 ):
    return True, result
  return False, result

def _query_transform(query):
  res = json.loads(open('src/wrappers/q.json').read())
  for p in res['ignore_phrases']:
    query = query.replace(p,'')
  for c in res['non_char']:
    query = query.replace(c,'')
  return query

def exe(query, userID):
  """
  Execute Search Function
  """
  suggestion = None
  fb = Facebook(userID, _uxy_core.environment.get('FACEBOOK', 'FB_PAGE_TOKEN'))
  fb.send_txt_msg('Searching...')

  # Raw Search
  ok, result = _search(query)
  if( ok ):
    if( 'searchinfo' in result['query'] ):
      if( 'suggestion' in result['query']['searchinfo'] ):
        suggestion = result['query']['searchinfo']['suggestion']

  # Transformed Search
  else:
    query = _query_transform(query)
    ok, result = _search(query)

  if( ok ):
    return {
      'results' : result['query']['search'],
      'suggestion' : suggestion
    } 
      

  return None
    





