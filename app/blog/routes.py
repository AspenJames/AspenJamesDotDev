from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from starlette.templating import Jinja2Templates
from react.render import render_component

from app.blog.utils import ssr_prefix
from app.constants import TEMPLATES_DIR

templates = Jinja2Templates(directory=TEMPLATES_DIR)
BLOG_TEMPLATE = 'layouts/blog.html'


class Index(HTTPEndpoint):
    async def get(self, request):
      component_path = ssr_prefix('Home.jsx')
      body = render_component(component_path)
      return templates.TemplateResponse('layouts/blog.html',
        {'request': request, 'title': 'Blog', 'body': body})


routes = [
    Route('/', Index)
]