"""
Dicitonary Function
"""

import json
import boto3
from _uxy_core import appconfig

global S3
global DBVersion
global WORDS_PER_MSG

DBVersion = 'v1'
S3 = boto3.resource('s3')
WORDS_PER_MSG = 40


def get(query):
  """
  Get word meaning
  """

  global S3
  global DBVersion

  query = query.lower().strip()
  index = query[0]
  s3Obj = S3.Object(appconfig['app:name']+'-uxy-app-'+appconfig['app:stage'],\
    'res/dictionaryDB'+DBVersion+'/index'+index.upper()+'.json')
  content = json.loads(s3Obj.get()['Body'].read().decode('utf-8'))
  if( query in content ):
    words = content[query].split()
    result = [" ".join(words[i : i + WORDS_PER_MSG])\
       for i in range(0, len(words), WORDS_PER_MSG)]
    return result

  return None


