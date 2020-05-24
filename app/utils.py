import sass

from .constants import APP_DIR

def compile_scss():
    sass.compile(dirname=('{}/static/scss'.format(APP_DIR),
                        '{}/static/css'.format(APP_DIR)),
                output_style='compressed')
