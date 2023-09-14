from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def Hello():
    return "Hello World!"


@app.route('/test')
def test():
    return "Hello World!_EXECUTED!"


@app.route('/test2/<name>')
def test2(name):
    return "Hello " + name


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['logemail']
        return redirect(url_for('test2', name=username))
    else:
        return redirect(url_for('fail'))


if __name__ == '__main__':
    app.run(debug=True)
