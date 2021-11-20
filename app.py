from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running, Ansh here"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
