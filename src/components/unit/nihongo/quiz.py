
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
from src.wrappers.wiki import WikiQuery

from src._functions.nihongo import generate_quiz


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  quizAns = int(convo_data.get_item(userID, 'nihongo_ans'))

  if( quizAns == optionMatched ):
    response = spiel.free_text('Correct! (Just type #exit to quit practicing)', 0)
  else:
    response = spiel.free_text('Wrong! (Just type #exit to quit practicing)', 0)
    alphaChoices = ['A','B','C','D']
    response += spiel.free_text('ANS: ' + alphaChoices[quizAns], 0)

  charType = convo_data.get_item(userID, 'nihongoCharType')
  charList = convo_data.get_item(userID, 'nihongoCharlist')
  quiz = generate_quiz.generate(userID, charType, charList)
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

  