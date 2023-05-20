from app import app
from flask import render_template, request, redirect, url_for
import check

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        taken_subjects = request.form.getlist('mycheckbox')
        electives = request.form.get('electives')
        print(f"taken subjects: {taken_subjects} \nelectives: {electives}")
        subject_timetable = check.main(taken_subjects, electives)
        # print(f"output: {subject_timetable}, {len(subject_timetable)}")
        # print(', '.join(subject_timetable[0])) # printing without [] and ""
        return redirect(url_for('results', subject_timetable = subject_timetable))
    return render_template('index.html', title='Home')

@app.route('/results/<subject_timetable>')
def results(subject_timetable):
    # print(f"output: {subject_timetable}, {len(subject_timetable)}")
    # print(', '.join(subject_timetable[0])) # printing without [] and ""
    return render_template('results.html', title='Results')
    # return f"RESULTS PAGE \nOutput: {subject_timetable}, {len(subject_timetable)}"