from sanic import Sanic, json, Request, file
from sanic_jinja2 import SanicJinja2

app = Sanic("main")
app.static("/static", "./static")
jinja = SanicJinja2(app, pkg_name="main", pkg_path="./templates")


@app.route('/')
async def index(request: Request):
	print(request.headers)
	headers = dict(request.headers)
	headers.pop("sec-ch-ua", None)
	headers.pop("sec-ch-ua-mobile", None)
	headers.pop("sec-ch-ua-platform", None)
	headers.pop("sec-fetch-user", None)
	return json(headers, 200)


@app.route('/favicon.ico')
async def favicon(request: Request):
	return file("./favicon.ico")
