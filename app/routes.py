from app import app
from flask import render_template, request
import check

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test = request.form.getlist('mycheckbox')
        print(test)
        return 'DONE'
    return render_template('index.html', title='Home')

@app.route('/results')
def results():
    return render_template('results.html', title='Results')