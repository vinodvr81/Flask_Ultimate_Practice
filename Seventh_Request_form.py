from flask import Flask,request

app = Flask(__name__)

@app.route('/')
@app.route('/theform')
def theform():
    return '''<form method="POST" action="/postprocess">
              <input type="text" name="name">
              <input type="text" name="age">
              <input type="submit" value="Submit">
              </form>'''


@app.route('/postprocess',methods=['POST'])
def postprocess():
    name = request.form['name']
    age = request.form['age']

    return "Hello Mr/Mrs. {}   ! Happy birthday : {} for your age".format(name,age)

if __name__ == '__main__':
    app.run(port=9000, debug=True)

# use browser service to test the post