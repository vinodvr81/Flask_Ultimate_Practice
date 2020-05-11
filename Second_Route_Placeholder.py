from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def say_hello(name):
    return "Hello Mr/Mrs." + name +  " !"

if __name__ == '__main__':
    app.run(port=6000, debug=True)