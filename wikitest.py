
import json
import time
from src.wrappers.wiki import WikiQuery

wq = WikiQuery()
  

pages = wq.search('synthesis')
print(pages)
pids = []
for res in pages['query']['search']:
  pids.append(str(res['pageid']))

page_descs = wq.get_description(pids)['query']['pages']

article_results = []

# Check Disambiguation
for pid in pids:
  print(page_descs[pid]['title'])
  if('description' in page_descs[pid]):
    print(page_descs[pid]['description'])
#   if('categories' in page_descs[pid]):
#     print('ambiguous')
#     pageInfo = wq.query_by_pageid(pid,1)['query']['pages'][0]['revisions'][0]['content']
#     print(pageInfo)
#   print('-')


# print('search> ')
# s = input()
# pinfo = wq.query_by_title(s)
# print(json.dumps(pinfo,indent=2))
