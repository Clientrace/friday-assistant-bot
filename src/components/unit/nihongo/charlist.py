
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
    convo_data.save_item(userID, 'nihongoCharlist', 'basic')
    quiz = generate_quiz.generate(userID, charType, 'basic')

  elif( optionMatched == 1 ):
    convo_data.save_item(userID, 'nihongoCharlist', 'combo')
    quiz = generate_quiz.generate(userID, charType, 'combo')

  else:
    return response

  quizChoices = []
  for item in quiz['choices']:
    quizChoices.append(item)

  quizSpiel = charType + " " + quiz['testChar'] + "\n"\
    + "Choices:\n"\
    + "A - " + quizChoices[0] + "\n"\
    + "B - " + quizChoices[1] + "\n"\
    + "C - " + quizChoices[2] + "\n"\
    + "D - " + quizChoices[3] + "\n"

  response += spiel.free_text(quizSpiel, 0)
  response += router.route(userID, 'nihongo.quiz')

  return response, valid


