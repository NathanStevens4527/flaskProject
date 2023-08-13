from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


# @app.route('/greet')
# def greet():
#     return 'Hello'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/temperature')
@app.route('/temperature/<celsius>')
def convert_celsius_to_fahrenheit(celsius=""):
    celsius = float(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"{celsius} in celsius is {fahrenheit} in fahrenheit"


if __name__ == '__main__':
    app.run()
