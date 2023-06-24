from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = "Hello, World!"
    return render_template("index.jinja.html", message=message)

if __name__ == '__main__':
    app.run()