
import json
import _uxy_core
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  if( optionMatched == 0 ):
    response = router.route(userID, 'dictionary.read', data)
  if( optionMatched == 1):
    response = router.route(userID, 'main')


  return response, valid




