from flask import Flask, request, render_template, flash
app = Flask(__name__)
app.secret_key = "homlko"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def index():
    flash("What's you name?")
    return render_template('index.html')

@app.route('/greet', methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
