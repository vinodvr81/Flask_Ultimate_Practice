from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def say_hello():
    return " Hello Mr. Vinod !"

@app.route('/json', methods=['GET','POST'])
def check_json():
    data = request.get_json()
    if data['name'] and data['age']:
        return jsonify({'name':data['name'], 'age':data['age']})
    else:
        return {}

if __name__ == '__main__':
    app.run(port=5000, debug=True)