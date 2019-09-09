
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

  qresult = search.search_article(data['data']['text'])
  if( len(qresult) == 0 ):
    response = spiel.get_display(userID, 'FS-02')
    return response, valid

  response = []
  topResult = qresult[0]['title']
  for r in qresult:
    # response += spiel.free_text(''+r['title']+' - '+r['description'], 0)
    response += spiel.btn_menu(''+r['title']+' - '+r['description'],
      [{"type" : "postback", "buttonName" : "READ", "payload" : "#read "+r['title'], "syns" : []}]
    )

  response += spiel.free_text('You can read more about the article by typing:\
    \n#read then the article name. Example: #read ' + topResult, 0)
  response += router.route(userID, 'main')
  return response, valid







