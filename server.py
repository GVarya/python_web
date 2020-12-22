from flask import Flask, render_template

server = Flask(__name__)

messages = [
{'username':'varya','text':'Привет'},
{'username':'opopio','text':'Пока'},
{'username':'fgh','text':'Привет и пока'}
]



@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href=/index>Index</a>'''


@server.route('/get_messages')


def get_messages():
    return{
    'messages': messages
}


@server.route('/index')
def index():
    name = 'Varya'
    return render_template("index.html")



@server.route('/day-<num>')
def day(num):
    return render_template(f"day-{num}.html")





server.run()
