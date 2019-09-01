from src.wrappers.wiki import WikiQuery


wq = WikiQuery()


resp = wq.search('enterprise')
print(resp)

