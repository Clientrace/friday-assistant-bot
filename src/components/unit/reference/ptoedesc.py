"""
Element Description
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

  userQuery = data['data']['text'].replace('#elementDesc','').strip()
  res = ptoe.get(userQuery.lower())
  if( res ):
    response = spiel.free_text(res['description'], 0)
    response += router.route(userID, 'reference.ptoe')

  return response, valid

