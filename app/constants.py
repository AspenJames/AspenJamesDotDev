import os

APP_DIR       = os.path.dirname(os.path.realpath(__file__))
MARKDOWN_DIR  = os.path.join(APP_DIR, 'static', 'markdown')
TEMPLATES_DIR = os.path.join('app', 'templates')
STATIC_DIR    = os.path.join('app', 'static')
SSR_DIR       = os.path.join(APP_DIR, 'static', 'js', 'ssr')