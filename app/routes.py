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
        sp51_23 = ', '.join(subject_timetable[0])
        sp52_23 = ', '.join(subject_timetable[1])
        sp53_23 = ', '.join(subject_timetable[2])
        sp51_24 = ', '.join(subject_timetable[3])
        sp52_24 = ', '.join(subject_timetable[4])
        sp53_24 = ', '.join(subject_timetable[5])
        return redirect(url_for('results', sp51_23 = sp51_23, sp52_23 = sp52_23, sp53_23 = sp53_23, sp51_24 = sp51_24, sp52_24 = sp52_24, sp53_24 = sp53_24))
    return render_template('index.html', title='Home')

@app.route('/results/<sp51_23>/<sp52_23>/<sp53_23>/<sp51_24>/<sp52_24>/<sp53_24>')
def results(sp51_23, sp52_23, sp53_23, sp51_24, sp52_24, sp53_24):
    # print(f"output: {subject_timetable}, {len(subject_timetable)}")
    # print(', '.join(subject_timetable[0])) # printing without [] and ""
    #return render_template('results.html', title='Results')
    return f"RESULTS PAGE <br/>Output: <br/>SP51 2023: {sp51_23}<br/>SP52 2023: {sp52_23}<br/>SP53 2023: {sp53_23}<br/>SP51 2024: {sp51_24}<br/>SP52 2024: {sp52_24}<br/>SP53 2024: {sp53_24}"