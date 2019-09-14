
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
  ptoe = json.loads(ptoeObj.get()['Body'].read().decode('utf-8'))

  if( query.strip().isdigit() ):
    index = int(query) - 1
    if( not (index < len(ptoe['elements']) or index == 0)):
      return None
  else:
    s3IndexObj = S3.Object(bucketName,
      'res/pTableofElementsDB'+DBVersion+'/index.json')
    searchIndex = json.loads(s3IndexObj.get()['Body'].read().decode('utf-8'))
    if( query in searchIndex ):
      index = searchIndex[query]
    else:
      return None

  element = ptoe['elements'][index]
  header = 'No. ' + str(index+1) + ' [ ' + element['name'] + ' ]\nSymbol: '+element['symbol']
  description = element['symbol'] + '\n' + element['summary']
  info = (element['appearance'] and 'Appearance: '+element['appearance'] or '') + '\n'\
    + (element['category'] and 'Category: '+element['category'] or '') + '\n'\
    + (element['atomic_mass'] and 'Atomic Mass: '+str(element['atomic_mass']) or '') +'\n'\
    + (element['density'] and 'Density: '+str(element['density']) or '') + '\n'\
    + (element['phase'] and 'Phase: '+element['phase'] or '') + '\n'\
    + (element['electron_configuration'] and 'Electron Config: '+element['electron_configuration'] or '')

  return {
    'element' : element['name'],
    'header' : header,
    'description' : description,
    'info' : info
  }



