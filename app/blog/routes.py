from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.templating import Jinja2Templates
from react.render import render_component

from app.blog.utils import (
  ssr_prefix, read_entry, EntryNotFound, EntryReadError
)
from app.constants import TEMPLATES_DIR

templates = Jinja2Templates(directory=TEMPLATES_DIR)
BLOG_TEMPLATE = 'layouts/blog.html'


class Index(HTTPEndpoint):
    async def get(self, request):
      component_path = ssr_prefix('Home.jsx')
      body = render_component(component_path)
      return templates.TemplateResponse('layouts/blog.html',
        {'request': request, 'title': 'Blog', 'body': body})


class Entry(HTTPEndpoint):
    async def get(self, request):
      entry = request.path_params['entry']

      try:
        markdown_content = read_entry(entry)
      except (EntryNotFound, EntryReadError) as e:
        return JSONResponse({'error': str(e)}, status_code=422)

      component_path = ssr_prefix('Entry.jsx')
      body = render_component(component_path, {
        'content': markdown_content
      })
      return templates.TemplateResponse('layouts/blog.html', {'request': request, 'title': entry, 'body': body})


routes = [
    Route('/', Index),
    Route('/{entry}', Entry)
]