from pollo_alimento import toSend
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    res = jsonify(toSend)
    return res

if __name__ == '__main__':
    app.run(debug=True)