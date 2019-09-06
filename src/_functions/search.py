"""
Chatbot Search Functionality
"""

import re
import json
import _uxy_core
from src.wrappers.wiki import WikiQuery
from _uxy_core.utility.api_wrappers.facebook import Facebook

wq = WikiQuery()

global WORDS_PER_MSG
WORDS_PER_MSG = 40

def build_query_response(query, pageIDs, pageInfos):
  responses = []
  for pageID in pageIDs:
    if( 'categories' not in pageInfos[pageID] ):
      if( 'description' in pageInfos[pageID] ):
        description = pageInfos[pageID]['description']
        responses.append({
          'title' : pageInfos[pageID]['title'],
          'description' : description
        })

  return responses


def search_article(query):
  pages = wq.search(query, 5)
  pageIDs = []
  for res in pages['query']['search']:
    pageIDs.append(str(res['pageid']))

  pageInfos = wq.get_description(pageIDs)['query']['pages']
  responses = build_query_response(query, pageIDs, pageInfos)
  return responses


def read_article(query):
  global WORDS_PER_MSG

  page = wq.query_by_title(query, 10)['query']['pages'][0]
  if( 'missing' in page ):
    return None

  if( 'extract' not in page ):
    return None

  pageContent = page['extract']
  words = pageContent.split()
  result = ["".join(words[i : i+WORDS_PER_MSG])\
     for i in range(0, len(words), WORDS_PER_MSG)]

  return result
 
 

