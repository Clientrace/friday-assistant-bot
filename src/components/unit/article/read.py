
import json
import _uxy_core
from src._functions import search
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from _uxy_core.utility.api_wrappers.facebook import Facebook


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  article_cache = convo_data.get_item(userID, 'article_cache')
  article_cache = json.loads(article_cache)
  response += spiel.free_text(article_cache.pop(0), 0)
  print("LENGHT: ")
  print(len(article_cache))
  if( len(article_cache) > 0 ):
    print("ROUTING TO ARTICLE CONTINUE")
    response += router.route(userID, 'article.continue')
    convo_data.save_item(userID, 'article_cache', json.dumps(article_cache))
  else:
    print("ROUTING TO MAIN")
    response += router.route(userID, 'main')

  return response, valid




