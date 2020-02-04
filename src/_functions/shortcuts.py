


def read(query):
  words = query.split(' ')
  if( len(words) > 1):
    if( '#search' in words[0].lower()):
      return 'article.article'

    if( '#read' in words[0].lower() ):
      return 'article.search'

    if( '#element' in words[0].lower() ):
      return 'reference.ptoe'

    if( '#elementDesc' in words[0].lower() ):
      return 'reference.ptoedesc'

  return None


