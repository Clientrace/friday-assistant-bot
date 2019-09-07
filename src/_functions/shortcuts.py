


def read(query):
  words = query.split(' ')
  if( len(words) > 1):
    if( '#read' in words[0].lower() ):
      return 'article.search'

  return None




