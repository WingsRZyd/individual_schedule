<<<<<<< HEAD
from datetime import datetime
from datetime import timedelta
=======
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
import json
from bs4 import BeautifulSoup
import requests


<<<<<<< HEAD
def add_json(day, date, time, place, data):
    if day:
        data[day + ', ' + date] = []
        for i, time1 in enumerate(time):
            time1 = time1.split('\u2013')
            one_str = {'time_begin': time1[0], 'time_end': time1[1], 'place': place[i]}
            data[day + ', ' + date].append(one_str)


def write_json_file(file, data):
    with open(file, "a", encoding="utf8") as out_file:
        json.dump(data, out_file, ensure_ascii=False, indent=4)


def empty_file(file):
    with open(file, "w", encoding="utf8") as file:
        file.close()
=======
def add_json(day, time, place, data):
    if day:
        data[day] = []
        for i in range(len(place)):
            time[i] = time[i].split('\u2013')
            one_str = {'time_begin': time[i][0], 'time_end': time[i][1], 'place': place[i]}
            data[day].append(one_str)


def write_json_file(file, data):
    out_file = open(file, "w", encoding='utf8')
    json.dump(data, out_file, ensure_ascii=False, indent=4)
    out_file.close()
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873


def find_info(soup, data):
    panels = soup.findAll(class_='panel panel-default')
    for panel in panels:
<<<<<<< HEAD
        title = find_day(panel)
        times = find_time(panel)
        places = find_place(panel)
        if title is not None and times:
            day = title[0]
            date = title[1]
            add_json(day, date, times, places, data)
=======
        d = find_day(panel)
        ts = find_time(panel)
        ps = find_place(panel)
        add_json(d, ts, ps, data)
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873


def find_day(panel):
    days = panel.find_all('h4', class_='panel-title')
    for day_str in days:
        only_day = day_str.get_text().split(',')
        day_param = only_day[0].strip()
<<<<<<< HEAD
        date_param = only_day[1].strip()
        title = [day_param.lower(), date_param.lower()]
        return title
=======
        return day_param.lower()
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873


def find_time(panel):
    times = panel.find_all('span', title='Время')
    time_array = []
    for time in times:
        time_param = time.get_text().strip()
        time_array.append(time_param)
    return time_array


def find_place(panel):
<<<<<<< HEAD
    places = panel.findAll(True, {"class": ["col-sm-3 studyevent-locations",
                                            "col-sm-3 studyevent-multiple-locations"]})
=======
    places = panel.findAll(True, {"class": ["col-sm-3 studyevent-locations", "col-sm-3 studyevent-multiple-locations"]})
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    place_array = []
    for place in places:
        street = place.get_text().split(',')
        place_param = street[0].strip()
        place_array.append(place_param)
    return place_array


<<<<<<< HEAD
def today_week():
    today = datetime.now().date()
    date = today - timedelta(datetime.now().weekday())
    return date


def few_weeks():
    weeks = []
    this_week = today_week()
    for i in range(0, 4):
        date = this_week + timedelta(weeks=i)
        weeks.append(date)
    return weeks


def main_teacher(index):
    empty_file('static/json/teacher.json')
=======
def main_teacher(index):
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    cookie = {
        "_culture": "ru",
        "value": "ru"
    }
<<<<<<< HEAD
    teacher_mas = {}
    weeks = few_weeks()
    for week in weeks:
        url_teacher = 'https://timetable.spbu.ru/WeekEducatorEvents/' + index + '/' + str(week)
        url_teacher_ru = requests.get(url_teacher, cookies=cookie, timeout=10).text
        html_teacher = BeautifulSoup(url_teacher_ru, "lxml")
        find_info(html_teacher, teacher_mas)
    write_json_file('static/json/teacher.json', teacher_mas)


def main_student(index):
    empty_file('static/json/student.json')
=======
    t = {}
    url_teacher = 'https://timetable.spbu.ru/WeekEducatorEvents/' + index
    url_teacher_ru = requests.get(url_teacher, cookies=cookie).text
    html_teacher = BeautifulSoup(url_teacher_ru, "lxml")

    find_info(html_teacher, t)
    write_json_file('static/json/teacher.json', t)


def main_student(index):
>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
    cookie = {
        "_culture": "ru",
        "value": "ru"
    }
<<<<<<< HEAD
    student_mas = {}
    weeks = few_weeks()
    for week in weeks:
        url_student = 'https://timetable.spbu.ru/MATH/StudentGroupEvents/Primary/'\
                      + index + '/' + str(week)
        url_student_ru = requests.get(url_student, cookies=cookie,timeout=10).text
        html_student = BeautifulSoup(url_student_ru, "lxml")
        find_info(html_student, student_mas)
    write_json_file('static/json/student.json', student_mas)


if __name__ == '__main__':
    main_student("334764")
    main_teacher("1446")
=======
    s = {}
    url_student = 'https://timetable.spbu.ru/MATH/StudentGroupEvents/Primary/' + index
    url_student_ru = requests.get(url_student, cookies=cookie).text
    html_student = BeautifulSoup(url_student_ru, "lxml")

    find_info(html_student, s)
    write_json_file('static/json/student.json', s)

>>>>>>> 6ff35856d1df8e93b49f87aa392c3f728bc15873
