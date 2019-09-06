


def read(query):
  words = query.split(' ')
  if( len(words) > 1):
    if( '#read' in words[0] ):
      return 'read_article'

  return None




