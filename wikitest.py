
import json
import time
from src.wrappers.wiki import WikiQuery

wq = WikiQuery()
  

pp = wq.search("Elon Musk's Tesla Roadster")
print(json.dumps(pp,indent=2))

# pp = wq.query_by_pageid('330338')
# print(pp['query']['pages'][0]['revisions'][0]['content'])









