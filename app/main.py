"""
Main application file for aspenjames.dev
see README.md for more information
"""

import os
import sass

from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app_dir = os.path.dirname(os.path.realpath(__file__))

templates = Jinja2Templates(directory='app/templates')


class Home(HTTPEndpoint):
    """Main application homepage"""
    async def get(self, request):
        """GET aspenjames.dev/"""
        return templates.TemplateResponse('index.html', {'request': request})


async def recompile(request):
    try:
        compile_scss()
        return JSONResponse({'200': 'OK'})
    except Exception as e:
        return JSONResponse({'error': e})


routes = [
    Route("/", Home),
    Route("/recompile", recompile),
    Mount('/static', app=StaticFiles(directory='app/static'), name='static'),
]

def compile_scss():
    sass.compile(dirname=('{}/static/scss'.format(app_dir),
                        '{}/static/css'.format(app_dir)),
                output_style='compressed')

# Compile SCSS at boot
compile_scss()
app = Starlette(debug=True, routes=routes)
