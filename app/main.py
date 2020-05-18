"""
TODO: module docstring
"""

import os
import sass

from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app_dir = os.path.dirname(os.path.realpath(__file__))

# Compile SCSS at boot
sass.compile(dirname=('{}/static/scss'.format(app_dir),
                      '{}/static/css'.format(app_dir)),
             output_style='compressed')

templates = Jinja2Templates(directory='app/templates')


class Home(HTTPEndpoint):
    """Main application homepage"""
    async def get(self, request):
        """GET aspenjames.dev/"""
        return templates.TemplateResponse('index.html', {'request': request})


routes = [
    Route("/", Home),
    Mount('/static', app=StaticFiles(directory='app/static'), name='static'),
]

app = Starlette(debug=True, routes=routes)
