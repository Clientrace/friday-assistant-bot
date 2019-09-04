
import json
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src._functions import search


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid
  index = data['data']['text']
  if( not index.isnum() ):
    return response, False

  qresult = json.loads(convo_data.get_item(userID, 'query_cache'))
  summary = search.get_summary(qresult['results'][index]['pageid'], 10)
  response = spiel.free_text(summary['extract'], 0)
  response += router.route(userID, 'view_more')

  return response, valid

  
