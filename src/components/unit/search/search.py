
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
    pass

  return response, valid

