
import _uxy_core
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    response = router.route(userID, "main")
    return response, valid

  if( optionMatched == 0 ):
    response = router.route(userID, "main")

  if( optionMatched == 1 ):
    print('Viewing updates')
    response = spiel.free_text(_uxy_core.update_notes, 0)
    response += router.route(userID, "main")


  return response, valid

  

