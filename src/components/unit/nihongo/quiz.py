
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  quizAns = convo_data.get_item(userID, 'nihongo_ans')
  userAns = data['data']['text']

  if( quizAns == userAns ):
    response = spiel.free_text('Correct!', 0)
  else:
    response = spiel.free_text('Wrong!', 0)

  return response, valid

  

