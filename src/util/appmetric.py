
from _uxy_core import appconfig
from _uxy_core.utility.aws_services.dynamodb import Dynamodb

global tablename
tablename = 'friday-app-metric'

def add_user():
  global tablename

  dynamodb = Dynamodb(tablename)
  itemKey = {
    'objname' : { 'S' : 'usernum' },
    'stage' : { 'S' : appconfig['app:stage'] }
  }
  data = dynamodb.increment(itemKey, 'val')
  print(data)


