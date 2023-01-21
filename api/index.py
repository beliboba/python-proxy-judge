from sanic import Sanic, json, Request, file, response
from sanic.exceptions import NotFound
from sanic_jinja2 import SanicJinja2

app = Sanic("main")
app.static("/static", "./static")
app.error_handler.add(NotFound, lambda r, e: response.empty(status=404))
jinja = SanicJinja2(app, pkg_name="main", pkg_path="./templates")


@app.route('/')
async def index(request: Request):
	print(request.headers)
	headers = dict(request.headers)
	return json(headers, 200)


@app.route('/favicon.ico')
async def favicon(request: Request):
	return await file("./static/favicon.ico")
