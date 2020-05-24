# Starlette.io

This is a pretty awesome little Python ASGI framework. A basic application
follows this format:

```python
async def home(request):
  return PlainTextResponse("hello!")

routes = [
  Route('/', home)
]

app = Starlette(routes=routes)
```