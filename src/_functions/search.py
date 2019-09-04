"""
Chatbot Search Functionality
"""

import json
import _uxy_core
from src.wrappers.wiki import WikiQuery
from _uxy_core.utility.api_wrappers.facebook import Facebook

wq = WikiQuery()

def transform_wikimarkup():
  pass

def find_disambiguation_page(pageIDs, pageInfos):
  for pid in pageIDs:
    if( 'categories' in pageInfos[pid] ):
      page = wq.query_by_pageid(pid, 1)['query']['pages'][0]
      return page
  return None

def exe(query):
  searchResults = []
  pages = wq.search(query)
  pageIDs = []
  for res in pages['query']['search']:
    pageIDs.append(str(res['pageid']))

  if( len(pageIDs) == 0 ):
    return None

  pageInfos = wq.get_description(pageIDs)['query']['pages']
  ambiguationPage = find_disambiguation_page(pageIDs, pageInfos)
  


