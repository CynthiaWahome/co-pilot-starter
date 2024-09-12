from flask import Flask
import time

app = Flask(__name__)

def seconds_since_epoch():
    epoch = time.time()
    return int(epoch)

@app.route("/")
def seconds():
    return seconds_since_epoch()
import time
from flask import Flask

app = Flask(__name__)

def seconds_since_epoch():
    epoch = time.time()
    return str(epoch)

def hours_since_epoch():
    epoch = time.time()
    return int(epoch // 3600)

@app.route("/")
def seconds():
    return str(seconds_since_epoch())

@app.route("/hours")
def hours():
    return str(hours_since_epoch())

if __name__ == "__main__":
    app.run(debug=True)

