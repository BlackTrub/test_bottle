# coding: utf-8

from bottle import Bottle
from bottle import run, static_file

from bottle import jinja2_template as template


app = Bottle()


@app.route('/')
def home_page():
    return template('template/home.html')


@app.route('/news')
def news_page():
    return template('template/news.html')


@app.error(404)
def error404(error):
    return template('template/404.html')


@app.get('/<filename:re:.*\.js>')
def static_js(filename):
    return static_file(filename, root='static/js')


@app.get('/<filename:re:.*\.css>')
def static_css(filename):
    return static_file(filename, root='static/css')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
