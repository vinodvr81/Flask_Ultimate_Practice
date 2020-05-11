from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
@app.route('/json')
def say_hello():
    a = {'Name': 'Vinod', 'Age': 38, 'Occupation' : { '2011': 'Intern',
                                                     '2014' : 'CAE data Analyst',
                                                     '2015': 'Research Engineer',
                                                     '2016' : 'Software Developer',
                                                     '2018' : 'Senior Software Developer'}}
    return jsonify(a)

if __name__ == '__main__':
    app.run(port=5000, debug=True)