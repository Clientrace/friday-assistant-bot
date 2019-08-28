
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  wikiQuery = WikiQuery()
  respText = wikiQuery.get_content(data['data']['text'])
  if( respText ):
    response = spiel.free_text(respText, 0)
    response += router.route(userID, 'main')
    return response, valid


  return response, valid

  

