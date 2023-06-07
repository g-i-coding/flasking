from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "I'm the king of the world, Bitches!"