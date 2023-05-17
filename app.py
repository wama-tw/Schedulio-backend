import aiofiles
import base64
from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from sanic.response import text
from sanic.response import json
from sanic_mail import Sanic_Mail
from env import HOST, PORT
from cors import add_cors_headers

app = Sanic("Schedulio")

# Fill in CORS headers
app.register_middleware(add_cors_headers, "response")

@app.route("/")
def hello(request):
    return text("Hi 😎")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
