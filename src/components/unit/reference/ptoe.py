
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery
from src._functions import ptoe


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  res = ptoe.get(data['data']['text'].lower())
  if( res ):
    response = []
    for r in res:
      response += spiel.free_text(r, 0)

  return response, valid
  



