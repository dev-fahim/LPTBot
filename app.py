import sys
from flask import Flask, request
from pprint import pprint
from pymessenger import Bot


app = Flask(__name__)

FB_ACCESS_TOKEN = "EAAfk8UkWEJgBAODAv9XAO8tgpInwHaaOEk1P9E9DDYV4ASAQA8PZCetnzlZCwErGP8Fd0L5eYIEYs6j83KoZAZB8jj0mZC0EJGJt9gqOaqew9frevrnb4Klo5oOikrfH9dmayryyio1ET0cAKvN9fsmfBHwqXBczlsr18l2YbcAZDZD"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
    # Web hook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    # Necessary Code that extract json data facebook send
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    # Extracting text message
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    # Echo Bot
                    response = messaging_text
                    bot.send_text_message(sender_id, response)

    return "ok", 200


def log(message):
    # previously it was print now I just Use Petty Print
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(port=80, use_reloader=True)