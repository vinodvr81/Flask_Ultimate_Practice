from flask import Flask,request

app = Flask(__name__)

@app.route('/')
@app.route('/fromURL')
def say_hello():
    name = request.args.get('name')
    age = request.args.get('age')

    return "Hello Mr/Mrs. {}   ! Happy birthday : {} for your age".format(name,age)

if __name__ == '__main__':

    app.run(port=8000, debug=True)
# give url input like shown below
#http://127.0.0.1:8000/?name=vinod&age=39
#http://127.0.0.1:8000/fromURL?name=Vishnu&age=42