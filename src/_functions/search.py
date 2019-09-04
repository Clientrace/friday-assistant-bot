"""
Chatbot Search Functionality
"""

import re
import json
import _uxy_core
from src.wrappers.wiki import WikiQuery
from _uxy_core.utility.api_wrappers.facebook import Facebook

wq = WikiQuery()

def parse_wikimarkup(content):
  responses = []
  print(content)
  headerRegEx = r'\=\=.*?\=\='
  topicRegEx = r'\[\[.*?\]\]'
  for section in content.split('\n\n')[1:]:
    articleTitles = re.findall(headerRegEx, section)
    if( len(articleTitles) > 0 ):
      if( 'see also' not in articleTitles[0].replace('=','').strip().lower() ):
        msgRes = 'In ' + articleTitles[0].replace('=','').strip()
        for title in articleTitles[1:]:
          msgRes += ', ' + title.replace('=','').strip()
        msgRes += '\n'
        articleTopics = re.findall(topicRegEx, section)
        if( len(articleTopics) > 0 ):
          msgRes += articleTopics[0].replace('[[','').replace(']]','')
          for topic in articleTopics[1:]:
            topic = topic.replace('[[', '').replace(']]', '')
            msgRes += ', ' + topic
          msgRes += '.'
        responses.append(msgRes)
    else: 
      articleTopics = re.findall(topicRegEx, section)
      if( len(articleTopics) > 0 ):
        msgRes = articleTopics[0].replace('[[','').replace(']]','')
        for topic in articleTopics:
          msgRes += ', ' + topic.replace('[[','').replace(']]','')
        msgRes += '.'
        responses.append(msgRes)
  return responses

def find_disambiguation_page(pageIDs, pageInfos):
  print('PAGE INFOS')
  print(pageInfos)
  for pid in pageIDs:
    if( 'categories' in pageInfos[pid] ):
      page = wq.query_by_pageid(pid, 1)['query']['pages'][0]
      return page
  return None

def check_result_relevance(querycheck, titlecheck):
  if( len(querycheck) > len(titlecheck) ):
    if titlecheck in querycheck:
      return True

  else:
    if querycheck in titlecheck:
      return True

  return False


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


def exe(query):
  pages = wq.search(query, 5)
  pageIDs = []
  for res in pages['query']['search']:
    pageIDs.append(str(res['pageid']))

  pageInfos = wq.get_description(pageIDs)['query']['pages']
  responses = build_query_response(query, pageIDs, pageInfos)
  return responses


  




