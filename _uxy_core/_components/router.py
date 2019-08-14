"""
Authored by Kim Clarence Penaflor
07/30/2019
version 0.0.2
Documented via reST

Chabot state router
"""

from _uxy_core import appconfig
from _uxy_core.utility.aws_services.dynamodb import Dynamodb
from _uxy_core._modules.e2e import input_parser
from _uxy_core._modules.e2e import view_parser
from _uxy_core._components import convo_data
from _uxy_core._components import spiel
from _uxy_core._components import persist
from datetime import datetime, timedelta

global DYNAMODB
DYNAMODB = Dynamodb(
  appconfig['app:name']+'uxy-session-'+appconfig['app:stage']
)

# Log Dynamodb Session Record Error
def log_error(userID):
  convo_data.increment(userID, 'errorLog')


# Check if user already exist
def user_exists(userID):
  global DYNAMODB
  record = DYNAMODB.get_item(
    {
      'userID' : {
        'S' : userID
      }
    }
  )
  return 'Item' in record


# Init user session
def init_session(userID,platform):
  global DYNAMODB
  DYNAMODB.put_item(
    {
      'userID' : {
        'S' : userID
      },
      'session' : {
        'S' : 'welcome'
      },
      'platform' : {
        'S' : platform
      },
      'errorLog' : {
        'N' : '0'
      },
      'datetimeCreated' : {
        'S' : str(datetime.now() + timedelta(hours=8))
      }
    }
  )


# Custom set rotue
def set_route(userID, session):
  global DYNAMODB
  key = {
    'userID' : {
      'S' : userID
    }
  }
  DYNAMODB.update_item(
    key,
    {
      'session' : {
        'Value' : {
          'S' : session
        }
      }
    }
  )


# Get current route
def get_route(userID):
  global DYNAMODB
  data = DYNAMODB.get_item(
    {
      'userID' : {
        'S' : userID
      }
    }
  )

  if( 'Item' in data ):
    errors = 0
    if( 'errorLog' in data['Item'] ):
      errors = data['Item']['errorLog']['N']
    if( 'session' in data['Item'] ):
      return data['Item']['session']['S'],errors
  
  return 'None','None'


# Set conversation Route
def route(userID, sessionName, data=None):
  global DYNAMODB
  key = {
    'userID' : {
      'S' : userID
    }
  }
  DYNAMODB.update_item(
    key,
    {
      'session' : {
        'Value' : {
          'S' : sessionName
        }
      }
    }
  )
  
  responses,altResponse,choices,optionMatched,valid,maxRetry = view_parser.exe(userID,sessionName,data)

  if( data ):
    unit = __import__('src.components.unit.'+sessionName,fromlist=[sessionName])
    responses, unitValid = unit.exe(userID, data, responses, altResponse, choices, optionMatched, valid, maxRetry)
    if( unitValid != None ):
      if( not unitValid ):
        if( maxRetry ):
          responses += route(userID, 'retry_fallback')
          convo_data.reset(userID, 'errorLog')
        else:
          log_error(userID)
      else:
        convo_data.reset(userID, 'errorLog')

  return responses


# Execute Route
def exe(userID, source, inputData, intentName):
  cur_session = None
  inputData = input_parser.exe(inputData)

  try:
    if( inputData['type'] == 'payload' ):
      if( 'PERSIST' in inputData['data']['payload'] ):
        prev_session,err = get_route(userID)
        if( prev_session not in persist.STATE_EXCEPTIONS ):
          cur_session = persist.ROUTES[inputData['data']['payload']]
          return route(userID, cur_session)

      if( 'FACEBOOK_WELCOME' in inputData['data']['payload'] ):
        cur_session = 'welcome'
        init_session(userID, 'facebook')

    if( intentName == 'Default Welcome Intent' ):
      cur_session = 'welcome'
      if( not user_exists(userID) ):
        init_session(userID, source)

    else:
      cur_session, errors = get_route(userID)
      inputData['errors'] = int(errors)
  except Exception as e:
    print('[ROUTE ERROR]: '+str(e))
    cur_session = 'error_fallback'

  return route(userID, cur_session, inputData)





