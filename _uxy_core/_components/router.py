"""
Authored by Kim Clarence Penaflor
07/30/2019
version 0.0.2
Documented via reST

Chabot state router
"""

import _uxy_core
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
  appconfig['app:name']+'-uxy-session-'+appconfig['app:stage']
)

# Log Dynamodb Session Record Error
def log_error(userID):
  convo_data.increment(userID, 'errorLog')


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
      'appversion' : {
        'S' : _uxy_core.appconfig['app:version']
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
def get_user_session(userID):
  global DYNAMODB
  data = DYNAMODB.get_item(
    {
      'userID' : {
        'S' : userID
      }
    }
  )

  return data

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

def _app_updates_check(session_data):
  if( not session_data ):
    return False

  if( 'appversion' not in session_data ):
    return True

  appversion = _uxy_core.appconfig['app:version']
  if( appversion != session_data['appversion']['S'] ):
    return True

  return False

# Execute Route
def exe(userID, source, inputData, intentName):
  cur_session = None
  inputData = input_parser.exe(inputData)

  user_session_data = get_user_session(userID)
  try:
    dataItem = None
    if( 'Item' in user_session_data ):
      dataItem = user_session_data['Item']
      if( 'errorLog' in dataItem and 'session' in dataItem ):
        cur_session = dataItem['session']['S']
        errors = dataItem['errorLog']['N']
      else:
        init_session(userID, 'facebook')
        cur_session = 'welcome'
    else:
      init_session(userID, 'facebook')
      cur_session = 'welcome'

    if( inputData['type'] == 'payload' ):
      if( 'FACEBOOK_WELCOME' in inputData['data']['payload'] ):
        cur_session = 'welcome'

      elif( 'PERSIST' in inputData['data']['payload'] ):
        if( _app_updates_check(dataItem) ):
          convo_data.save_item(userID, 'appversion',\
            _uxy_core.appconfig['app:version'])
          return route(userID, 'app_update')

        if( cur_session not in persist.STATE_EXCEPTIONS ):
          cur_session = persist.ROUTES[inputData['data']['payload']]
          return route(userID, cur_session)

    if( _app_updates_check(dataItem) ):
      convo_data.save_item(userID, 'appversion',\
        _uxy_core.appconfig['app:version'])
      return route(userID, 'app_update')

    inputData['errors'] = int(errors)
  except Exception as e:
    print('[ROUTE ERROR]: '+str(e))
    cur_session = 'error_fallback'

  print('CURSESSION: ')
  print(cur_session)
  return route(userID, cur_session, inputData)



