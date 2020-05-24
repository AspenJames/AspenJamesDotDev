import os

from app.constants import MARKDOWN_DIR
from app.constants import SSR_DIR

class EntryNotFound(BaseException): pass;
class EntryReadError(BaseException): pass;

def ssr_prefix(filename):
  return os.path.join(SSR_DIR, filename)

def read_entry(entry):
  filename = entry + ".md"
  filepath = os.path.join(MARKDOWN_DIR, filename)

  if not os.path.exists(filepath):
    raise EntryNotFound("{} not found".format(filepath))

  with open(filepath) as file:
    try:
      markdown = file.read()
    except Exception as e:
      raise EntryReadError(e)

  return markdown
