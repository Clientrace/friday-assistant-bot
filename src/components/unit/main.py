
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  if( optionMatched == 0 ):
    response = router.route(userID, 'article.article')

  if( optionMatched == 1 ):
    response = router.route(userID, 'dictionary.search')

  # if( optionMatched == 2 ):
  #   response = router.route(userID, 'reference.reference')

  return response, valid

  
