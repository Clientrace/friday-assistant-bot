
import json
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src._functions import search


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  qresult = search.exe(data['data']['text'], userID)
  response = []
  if( 'suggestion' in qresult ):
    if( qresult['suggestion'] ):
      response += spiel.mod_text(userID, "FS-06", ":title:", qresult['suggestion'])

  if( len(qresult['results']) == 0 ):
    response = spiel.text(userID, 'FS-02')
    response += router.route(userID, 'main')

  if( len(qresult['results']) == 1 ):
    summary = search.get_summary(qresult['results'][0]['pageid'])
    response += spiel.free_text(summary['title'], 0)
    response += spiel.free_text(summary['extract'], 0)

  if( len(qresult['results']) > 1 ):
    result_item = qresult['results'].pop(0)
    summary = search.get_summary(result_item['pageid'])
    response += spiel.free_text(summary['extract'], 0)
    relatedArticles = '*Related Articles*\n'
    for r in qresult['results']:
      relatedArticles += '* ' + r['title'] + '\n'

    response += spiel.free_text(relatedArticles, 0)

  return response, valid




