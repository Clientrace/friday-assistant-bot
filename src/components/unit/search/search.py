
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src._functions import search


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  qresult = search.exe(data['data']['text'], userID)
  if( len(qresult['results']) == 1 ):
    response = []
    if( 'suggestion' in qresult ):
      response += spiel.mod_text(userID, "FS-06", ":title:", qresult['suggestion'])
    summary = search.get_summary(qresult['results'][0]['pageid'])
    response += spiel.free_text('Title: ' + summary['title'], 0)
    response += spiel.free_text(summary['extract'], 0)

  return response, valid


