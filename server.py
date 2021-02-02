from flask import Flask, render_template, request
import time



server = Flask(__name__)

messages = [
{'username':'varya','text':'Привет', "timestamp": time.time()},
{'username':'opopio','text':'Пока', "timestamp": time.time()},
{'username':'fgh','text':'Привет и пока', "timestamp": time.time()}
]



@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href=/index>Index</a>'''


@server.route('/get_messages')


def get_messages():
    after = float(request.args["after"])
    result = []

    for message in messages:
        if message["timestamp"] > after:
            result.append(message)
    return{
        "messages": result
}


@server.route('/index')
def index():
    name = 'Varya'
    return render_template("index.html")



@server.route('/day-<num>')
def day(num):
    return render_template(f"day-{num}.html")


@server.route('/send_messages')

def send_messages():


    messages.append({
        "username": request.json["username"],
        "text": request.json["text"],
        "timestamp": time.time()
    })



server.run()
