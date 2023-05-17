from sanic import Sanic
from sanic.response import json
from sanic_mail import Sanic_Mail
from env import MAIL_SENDER, MAIL_SENDER_PASSWORD, MAIL_SEND_HOST, MAIL_SEND_PORT, MAIL_TLS, MAIL_START_TLS, MAIL_HOST, MAIL_PORT
from database import TOKEN

app = Sanic(__name__)
app.config.update({
    'MAIL_SENDER': MAIL_SENDER,
    'MAIL_SENDER_PASSWORD': MAIL_SENDER_PASSWORD,
    'MAIL_SEND_HOST': MAIL_SEND_HOST,
    'MAIL_SEND_PORT': MAIL_SEND_PORT,
    'MAIL_TLS': MAIL_TLS,
    'MAIL_START_TLS': MAIL_START_TLS
})
sender = Sanic_Mail(app)


@app.get('/mail/send')
async def send(request):
    if request.args.get("token") != TOKEN :
        return json({"result": "401 Unauthorized"})
    if request.args.get("email") == None:
        return json({"result": "400 Bad Request"})
    await request.app.ctx.send_email(
        targetlist = request.args.get("email"),
        subject = "測試傳送",
        content = "測試傳送uu"
    )
    return json({"result": "200 OK"})


if __name__ == "__main__":
    app.run(host=MAIL_HOST, port=MAIL_PORT, debug=True)