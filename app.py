from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "<p>Roberto ist ein G</p>"

if __name__ == '__main__':
    application.run()