from sanic import Sanic, json, Request, file, response
from sanic.exceptions import NotFound
from sanic_jinja2 import SanicJinja2

app = Sanic("main")
app.static("/static", "./static")
app.error_handler.add(NotFound, lambda r, e: response.empty(status=404))
jinja = SanicJinja2(app, pkg_name="main", pkg_path="./templates")


@app.route('/')
async def index(request: Request):
	try:
		headers = {}
		for key, value in request.headers.items():
			if isinstance(value, list):
				value = ';'.join(value)
			headers[key] = value
		return json(headers, 200)
	except Exception as e:
		return json({'error': str(e)}, 500)


@app.route('/favicon.ico')
async def favicon(request: Request):
	return await file("./static/favicon.ico")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)
