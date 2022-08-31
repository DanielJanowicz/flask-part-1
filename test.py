from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dan!'

@app.route('/careers')
def careers():
    return 'THis is the career page!'

@app.route('/dashboard')
def dashboard():
    return 'This is the website dashboard!'



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)