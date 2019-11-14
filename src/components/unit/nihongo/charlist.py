
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery

from src._functions.nihongo import generate_quiz


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  charType = convo_data.get_item(userID, 'nihongoCharType')

  if( optionMatched == 0 ):
    convo_data.save_item(userID, 'charlist', 'basic')
    quiz = generate_quiz.generate(userID, charType, 'basic')

  if( optionMatched == 0 ):
    convo_data.save_item(userID, 'charlist', 'combo')
    quiz = generate_quiz.generate(userID, charType, 'basic')

  quizChoices = []
  for item in quiz['choices']:
    quizChoices.append({
      'data' : item
    })

  response = spiel.free_text( charType + " " + quiz['testChar'], 0)
  response += spiel.quick_reply(userID, 'FS-14', quizChoices)
  router.route(userID, 'quiz')

  return response, valid

