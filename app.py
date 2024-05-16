from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Home Page",
        heading="Welcome",
        content="This is the home page.",
    )


if __name__ == "__main__":
    app.run()
