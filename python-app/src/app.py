from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, here is my new flask app!"

if __name__ == "__main__":
    app.run()
