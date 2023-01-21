from sanic import Sanic, json, Request, file, response
from sanic.exceptions import NotFound

app = Sanic("main")
app.static("static", "static")
app.error_handler.add(NotFound, lambda r, e: response.empty(status=404))


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
	return await file('./static/favicon.ico')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=1337, debug=True)
