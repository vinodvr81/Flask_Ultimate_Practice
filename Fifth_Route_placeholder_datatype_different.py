from flask import Flask

app = Flask(__name__)

@app.route('/<string:name>/<int:id>/<int:age>')
def say_hello(name,id,age):
    return "Hello Mr/Mrs." + name +  " !" + " your id is: " + str(id) + " happy birthday : " + str(age)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
#input URL should be like below
#http://127.0.0.1:5000/Vinod/16/39