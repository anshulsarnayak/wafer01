from wsgiref import simple_server

import os
from wsgiref import simple_server

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running, Ansh here, WhAT'S UP?"

port = int(os.getenv("PORT", 5000))

if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()