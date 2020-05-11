# use postman to see the output and not the browser

from flask import Flask

app = Flask(__name__)

@app.route('/<name>', methods=['POST'])
def say_hello(name):
    return "Hello Mr/Mrs." + name +  " !"

if __name__ == '__main__':
    app.run(port=7000, debug=True)