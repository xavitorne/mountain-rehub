from rehub import app
from flask import request, redirect, url_for, abort, \
     render_template, flash, g

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/<page_name>')
def specific_page(page_name):
    return render_template('%s' % page_name)

