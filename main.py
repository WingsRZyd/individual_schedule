<<<<<<< HEAD
=======

>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
import json

from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

<<<<<<< HEAD
import find_student_page
=======
import find_student_json
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
import find_teacher_json
import free_time
import timetable_json

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
<<<<<<< HEAD
    """main page"""
=======
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    return render_template('index.html')


def find_teacher(input_form):
<<<<<<< HEAD
    """information about teachers"""
    find_teacher_json.main_teacher(input_form)


def find_student(input_form):
    """information about id student"""
    id_student = find_student_page.main_student(input_form)
    timetable_json.main_student(id_student)


# def count_person(person):
#     persons = person.split(",")
#     return len(persons)
#

# def decide_compare(teachers, students):
#     teachers = teachers.split(",")
#     students = students.split(",")
#     if teachers != "" and students != "":
#         if len(teachers) == len(students) == 1:
#             find_student(students)
#             find_teacher(teachers)
#         else:
#             for teacher in teachers:
#                 find_teacher(teacher)  # add in file all teachers
#                 # new fun compare_teachers
#             for s in range(0, len(students)):
#                 students[s] = find_student_page.main_student(s)
#                 # new fun compare_students
#             # compare together
#     else:
#         if teachers != "" and students == "":
#             for teacher in teachers:
#                 find_teacher(teacher)
#                 # only teachers
#         if teachers == "" and students != "":
#             for student in students:
#                 find_student(student)
#                 # only students
=======
    find_teacher_json.main_teacher(input_form)
    return render_template('index.html')


def find_student(input_form):
    id_student = find_student_json.main_student(input_form)
    timetable_json.main_student(id_student)
    return render_template('index.html')
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873


@app.route('/find', methods=["GET", "POST"])
def find():
<<<<<<< HEAD
    """main page with information about teachers or return result timetable"""
    if request.method == 'POST':
        student = request.form.get('student')
        teacher = request.form.get('teacher')
        flag_place = 'flag_place' in request.form
=======
    if request.method == 'POST':
        student = request.form.get('student')
        teacher = request.form.get('teacher')
        # if not student:
        #     flash('Группа студента не введена!')
        # elif not teacher:
        #     flash('ФИО преподавателя не введено!')
        # else:
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
        student_result = jsonify(student)
        find_student(student_result.json)
        teacher_result = jsonify(teacher)
        find_teacher(teacher_result.json)
<<<<<<< HEAD
        if one_teacher_table(str(flag_place)) is not None:
            return render_template('table.html')
        return render_template('index.html', student=student,
                               teacher=teacher, flag_place=flag_place,
                               checkbox_checked="checked" if flag_place else "")
    return render_template('index.html')


def one_teacher_table(flag):
    """if found one teacher, show result page"""
    with open("static/json/info_teacher.json", encoding="utf8") as file:
        data = json.load(file)
    res = data['teacher']
    if len(res) == 1:
        for i in res:
            if i['index']:
                result = i['index']
                timetable_json.main_teacher(result)
                free_time.main(flag)
                return result
    return None


def one_teacher():
    """if on the main mage is only one card - pull out the id"""
    with open("static/json/info_teacher.json", encoding="utf8") as file:
        data = json.load(file)
=======
    return render_template('index.html')


def one_teacher():
    f = open('static/json/info_teacher.json', encoding='utf-8')
    data = json.load(f)
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    res = data['teacher']
    for i in res:
        if i['index']:
            return i['index']
<<<<<<< HEAD
    return ""
=======
    f.close()
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873


@app.route("/time", methods=["GET", "POST"])
def timetable():
<<<<<<< HEAD
    """show result page"""
    result = request.form.get('id')
    flag = request.form.get('flag_place')
    if result == "":
        result = one_teacher()
    timetable_json.main_teacher(result)
    free_time.main(str(flag))
=======
    result = request.form.get('id')
    if result == "":
        result = one_teacher()
    timetable_json.main_teacher(result)
    free_time.main()
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    return render_template('table.html')


if __name__ == '__main__':
    app.run(port=5000)
