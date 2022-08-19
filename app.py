from flask import jsonify, make_response
from config import APP, db
from db.schemas.schedule import Schedule

db.create_all()


@APP.route('/')
def root_page():
    return 'Welcome to the root page!'


@APP.route('/schedule/days', methods=['GET'])
def get_lessons() -> str:
    """
    Get all day schedules from the database\n
    :return: String format of all tasks in the database
    """
    rows = Schedule.get_all_rows()
    return str(rows)


@APP.route('/schedule/add_day', methods=['GET', 'POST'])
def add_day() -> str:
    """
    Add a new day to the schedule\n
    :return: String
    """
    row = Schedule.insert_row('first_lesson', 'second_lesson', 'third_lesson', 'fourth_lesson', 'fifth_lesson')
    return str(row)


@APP.route('/schedule/days/<int:day_id>', methods=['GET'])
def get_day(day_id: int) -> str:
    """Method to get a day schedule by its id\n
    :param day_id: id of the day to get from the database
    :return: string format of the day schedule
    """
    row = Schedule.get_row(day_id)
    return str(row)


@APP.route('/schedule/days/<int:day_id>/lesson/<int:lesson_index>', methods=['GET'])
def get_lesson(day_id: int, lesson_index: int) -> str:
    """Method to get a lesson by its index\n
    :param day_id: id of the day schedule to get from the database
    :param lesson_index: index of the lesson to get from the day schedule
    :return: string format of the lesson
    """
    schedule_inst = Schedule.get_row(day_id)
    return str(schedule_inst.get_lesson(lesson_index))


@APP.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    APP.run(debug=True)
