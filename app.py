from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hey man hello new!'

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')
