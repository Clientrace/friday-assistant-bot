
import json
import time
from src.wrappers.wiki import WikiQuery

wq = WikiQuery()
  

pp = wq.search("Big bang theory")
print(json.dumps(pp,indent=2))










