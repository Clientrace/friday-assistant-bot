
import json
import time
from src.wrappers.wiki import WikiQuery

wq = WikiQuery()
  


pp = wq.query_by_pageid('2996918')
print(json.dumps(pp,indent=2))









