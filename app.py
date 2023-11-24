from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f')
@app.route('/f/<fahrenheit>')
def f(fahrenheit=10):
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return f"{fahrenheit} is {celsius}"


if __name__ == '__main__':
    app.run()
