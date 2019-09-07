
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

  response = []
  userQuery = data['data']['text'].replace('#read','').strip()
  result = search.read_article(userQuery)
  if( result ):
    response += spiel.free_text(result.pop(0), 0)
    if( len(result) > 0 ):
      response += router.route(userID, 'article.read')
      convo_data.save_item(userID, 'article_cache', json.dumps(result))
    else:
      response = router.route(userID, 'main')
  else:
    response = spiel.text(userID, "FS-02")

  return response, valid

