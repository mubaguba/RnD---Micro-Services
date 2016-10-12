from flask import Flask,jsonify

app = Flask(__name__)
@app.route('/',methods=['GET'])
def mainPage():
    return "This is the main page"

@app.route('/World' ,methods =['GET'])
def world():
    return "This is my world"
@app.route('/Hello', methods = ['GET'])
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
