
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  if( optionMatched == 0 ):
    convo_data.save_item(userID, 'nihongoCharType', 'katakana')

  if( optionMatched == 1 ):
    convo_data.save_item(userID, 'nihongoCharType', 'hiragana')

  response = router.route( userID, "nihongo.charlist")

  return response, valid

  

