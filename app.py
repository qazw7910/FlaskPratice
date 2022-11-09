from flask import Flask, url_for, request, render_template
from markupsafe import escape
from flask_bootstrap import Bootstrap

app = Flask(__name__)



@app.route('/')
def hello(name=None):
    paragraph = ['section1', 'section2', 'section3', 'section4']

    return render_template('hello.html', title='ABCDEF', data=paragraph)


if __name__ == '__main__':
    app.run(debug=True)
