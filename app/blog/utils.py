import os

from app.constants import SSR_DIR

def ssr_prefix(filename):
  return os.path.join(SSR_DIR, filename)