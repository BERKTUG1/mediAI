from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Roberto ist ein G</p>"

if __name__ == '__main__':
    app.run()