
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

  qresult = search.exe(data['data']['text'], userID)
  response = []

  if( not qresult ):
    response = spiel.text(userID, 'FS-02')
    response += router.route(userID, 'main')
    return response, valid

  if( 'suggestion' in qresult ):
    if( qresult['suggestion'] ):
      response += spiel.mod_text(userID, "FS-06", ":title:", qresult['suggestion'])

  if( len(qresult['results']) == 1 ):
    summary = search.get_summary(qresult['results'][0]['pageid'], 10)
    response += spiel.free_text(summary['title'], 0)
    response += spiel.free_text(summary['extract'], 0)
    response += router.route(userID, 'main')

  if( len(qresult['results']) > 1 ):
    fb = Facebook(userID, _uxy_core.environment.get('FACEBOOK', 'FB_PAGE_TOKEN'))
    count = 0
    for r in qresult['results']:
      count += 1
      summary = search.get_summary(r['pageid'], 1)
      botMsg = str(count) + ' ' + summary['extract']
      fb.send_txt_msg(botMsg)

    
    convo_data.save_item(userID, 'query_cache', json.dumps(qresult))
    response += router.route(userID,'search.view_more')


  return response, valid




