import json
import random
from _uxy_core._components import spiel
from _uxy_core._components import convo_data

global DBSRC
DBSRC = 'src/_functions/nihongo/'

def generate(userID, qtype, charlist):
  charJson = json.loads(open(DBSRC + qtype + '_' + charlist + '.json').read())
  testChar = random.choice(list(charJson))
  choices = [None, None, None, None]
  ans = random.randint(0,3)
  choices[ans] = charJson[testChar]
  for i in range(0,4):
    if( not choices[i] ):
      choices[i] = charJson[random.choice(list(charJson))]

  convo_data.save_item(userID, 'nihongo_ans', str(ans))
  return {
    'testChar' : testChar,
    'choices' : choices
  }

