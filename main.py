## Importing the flask package
from flask import Flask

app = Flask(__name__)

## Developing different routes
@app.route('/')
def home():
    return 'This is the homepage!'

@app.route('/help')
def help():
    return 'This is the help page!'

@app.route('/contact')
def contact():
    return 'This is the contact page!'

## Developing local host
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)