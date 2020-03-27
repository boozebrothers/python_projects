import time
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
messages = [
    {'username': 'jack', 'text': 'Hello', 'time': time.time()},
    {'username': 'mary', 'text': 'Hi, jack', 'time': time.time()},
]

users = {
    # username: password
    'jack': 'black',
    'mary': '12345'
}


@app.route("/")
def home():
    return "Home Page"


@app.route("/status")
def status():
    return {
        "status": True,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'users_count': len(messages),
        'messages_count': len(users)
    }


@app.route("/history")
def history():
    """
        request: ?after=timestamp
        response: {
            "messages": [
                    {"username": "str", "text": "str", "time": float}
                    ...
            ]
        }
        """
    after = float(request.args['after'])
    filtered_messages = [message for message in messages if after < message['time']]
    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send():
    """
    request: {"username": "str", "password": "str", "text": "str"}
    response: {"ok": true}
    """
    data = request.json  # JSON to dictionary
    username = data['username']
    password = data['password']
    text = data['text']

    # if User created -> check the password of the User
    # or new User will be registered
    if username in users:
        real_password = users[username]
        if real_password != password:
            return {"ok": False}
    else:
        users[username] = password

    new_message = {'username': username, 'text': text, 'time': time.time()}
    messages.append(new_message)

    return {"ok": True}


app.run()
