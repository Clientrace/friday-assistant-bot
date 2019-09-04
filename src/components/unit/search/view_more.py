
import json
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src._functions import search


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  if( optionMatched == 0 ):
    response = router.route(userID, 'search.view')

  return response, valid

  
