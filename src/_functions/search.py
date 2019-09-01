"""
Chatbot Search Functionality
"""

from src.wrappers.wiki import WikiQuery

def exe(msg):
  """
  Execute Search Function
  """
  wikiQuery = WikiQuery()
  respText = wikiQuery.get_content(msg)
  pass

