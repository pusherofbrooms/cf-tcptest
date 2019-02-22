from flask import Flask
import os
import socket
import time

testhosts = os.getenv("testhosts").split(",")
testports = os.getenv("testports").split(",")

socket.setdefaulttimeout(5)
s = socket.socket()

app = Flask(__name__)

port = int(os.getenv("PORT", 9099))

while True:
    time.sleep(5)
    for h in testhosts:
        ip = socket.gethostbyname(h)
        for p in testports:
            p = int(p)
            s = socket.socket()
            result = s.connect_ex((ip, p))
            s.close()
            if result:
                print("there was a problem connecting to %s:%d" % (h, p))
            else:
                print("connected successfully to %s:%d" % (h, p))


@app.route("/")
def hello_world():
    return "Hello world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
