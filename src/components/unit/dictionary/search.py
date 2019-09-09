
import json
from src._functions import dictionary
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data

def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  response = []
  userQuery = data['data']['text']
  result = dictionary.get(userQuery)
  if( result ):
    response += spiel.free_text(result.pop(0), 0)
    if( len(result) > 0 ):
      response += router.route(userID, 'article.continue')
      convo_data.save_item(userID, 'article_cache', json.dumps(result))
    else:
      response += router.route(userID, 'main')
  else:
    response = spiel.text(userID, 'FS-07')
    response += router.route(userID, 'main')

  return response, valid


