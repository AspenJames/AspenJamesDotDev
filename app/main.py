"""
Main application file for aspenjames.dev
see README.md for more information
"""

from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from react.conf import settings

from .constants import STATIC_DIR
from .constants import TEMPLATES_DIR
from .blog.routes import routes as blog_routes
from .utils import compile_scss

templates = Jinja2Templates(directory=TEMPLATES_DIR)

settings.configure(
    RENDER_URL='http://node:9009/render'
)


class Home(HTTPEndpoint):
    """Main application homepage"""
    async def get(self, request):
        """GET aspenjames.dev/"""
        return templates.TemplateResponse('index.html', {'request': request})


async def recompile(request):
    """Recompile scss assets"""
    try:
        compile_scss()
        return JSONResponse({'200': 'OK'})
    except Exception as e:
        return JSONResponse({'error': str(e)})

routes = [
    Route("/", Home),
    Route("/recompile", recompile),
    Mount('/blog', routes=blog_routes),
    Mount('/static', app=StaticFiles(directory=STATIC_DIR), name='static'),
]


# Compile SCSS at boot
compile_scss()
app = Starlette(debug=True, routes=routes)
