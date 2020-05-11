from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return " Hello Mr. Vinod !"

if __name__ == '__main__':
    app.run(port=5000, debug=True)