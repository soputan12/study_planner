from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/results')
def results():
    return render_template('results.html', title='Home')