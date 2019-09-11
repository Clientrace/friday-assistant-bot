"""
Periodic Table of Elements
"""

import json
import boto3
from _uxy_core import appconfig

global S3
global DBVersion

DBVersion = 'v1'
S3 = boto3.resource('s3')

def get(query):

  global S3
  global DBVersion
  
  query = query.strip()
  
  bucketName = appconfig['app:name']+'-uxy-app-'+appconfig['app:stage']
  ptoeObj = S3.Object(bucketName,
    'res/pTableofElementsDB'+DBVersion+'/ptoe.json')
  s3IndexObj = S3.Object(bucketName,
    'res/pTableofElementsDB'+DBVersion+'/index.json')
  searchIndex = json.loads(s3IndexObj.get()['Body'].read().decode('utf-8'))
  ptoe = json.loads(ptoeObj.get()['Body'].read().decode('utf-8'))
  if( query in searchIndex ):
    response = []
    index = searchIndex[query]
    element = ptoe['elements'][index]
    response.append(
      'No. ' + str(index) + ' [' + element['name'] + '] \nSymbol: '\
       + element['symbol'] + '\n' \
       + element['summary']
    )

    response.append(
      'Appearance: ' + element['appearance'] + '\n' \
      + 'Category: ' + element['category'] + '\n' \
      + 'Atomic Mass: ' + str(element['atomic_mass']) + '\n' \
      + 'Density: ' + str(element['density']) + '\n' \
      + 'Phase: ' + element['phase'] + '\n' \
      + 'Electron Configuration: ' + element['electron_configuration']
    )
    return response

  return None





