
"""
Periodic Table of Elements Reference
"""

from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery
from src._functions import ptoe


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  res = ptoe.get(data['data']['text'].lower().replace('#element',''))
  if( res ):
    response = spiel.free_text(res['header'], 0)
    response += spiel.btn_menu(res['info'],
      [{"type" : "postback", "buttonName" : "Description", "payload" : "#elementDesc "+res['element'], "syns" : []}]
    )
    response += router.route(userID, 'main')

  return response, valid
  


