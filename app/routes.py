from app import app
from flask import render_template, request
import check

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        taken_subjects = request.form.getlist('mycheckbox')
        electives = request.form.get('electives')
        print(f"taken subjects: {taken_subjects} \nelectives: {electives}")
        subject_timetable = check.main(taken_subjects, electives)
        print(f"output: {subject_timetable}, {len(subject_timetable)}")
        return 'DONE'
    return render_template('index.html', title='Home')

@app.route('/results')
def results():
    return render_template('results.html', title='Results')