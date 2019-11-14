import json
import random
from _uxy_core._components import spiel
from _uxy_core._components import convo_data

global DBSRC
DBSRC = 'src/_functions/nihongo/'

def generate(userID, qtype, charlist):
  charJson = json.loads(open(DBSRC + qtype + '_' + charlist + '.json').read())
  print(list(charJson))
  testChar = random.choice(list(charJson))
  choices = [
    charJson[testChar],
    charJson[random.choice(list(charJson))],
    charJson[random.choice(list(charJson))],
    charJson[random.choice(list(charJson))]
  ]

  random.shuffle(choices)
  convo_data.save_item(userID, 'nihongo_ans', charJson[testChar])
  return {
    'testChar' : testChar,
    'choices' : choices
  }




