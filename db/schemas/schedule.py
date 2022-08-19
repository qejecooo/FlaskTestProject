from config import db


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_lesson = db.Column(db.String)
    second_lesson = db.Column(db.String)
    third_lesson = db.Column(db.String)
    fourth_lesson = db.Column(db.String)
    fifth_lesson = db.Column(db.String)

    def __init__(self, first_lesson: str, second_lesson: str, third_lesson: str, fourth_lesson: str, fifth_lesson: str):
        self.first_lesson = first_lesson
        self.second_lesson = second_lesson
        self.third_lesson = third_lesson
        self.fourth_lesson = fourth_lesson
        self.fifth_lesson = fifth_lesson

    def __repr__(self):
        return "(%s, %s, %s, %s, %s, %s)" % (
            self.id, self.first_lesson, self.second_lesson, self.third_lesson, self.fourth_lesson, self.fifth_lesson)

    @classmethod
    def get_row(cls, row_id: int) -> 'Schedule':
        """
        Get a day schedule from the database by its id\n
        :param row_id: id of the day schedule to get from the database
        :return: class instance of the table
        """
        row = db.session.query(Schedule).filter_by(id=row_id).first()
        return row

    @classmethod
    def get_all_rows(cls) -> list:
        """
        Get all day schedules from the database\n
        :return: string format of all rows in the database
        """
        rows = db.session.query(Schedule).all()
        return rows

    @classmethod
    def insert_row(cls, first_lesson, second_lesson, third_lesson, fourth_lesson, fifth_lesson) -> 'Schedule':
        """
        Insert a day schedule into the database\n
        :param first_lesson: first lesson of the day to insert into the database
        :param second_lesson: second lesson of the day to insert into the database
        :param third_lesson: third lesson of the day to insert into the database
        :param fourth_lesson: fourth lesson of the day to insert into the database
        :param fifth_lesson: fifth lesson of the day to insert into the database
        :return: class instance of the table
        """
        schedule_instance = Schedule(first_lesson, second_lesson, third_lesson, fourth_lesson, fifth_lesson)
        db.session.add(schedule_instance)
        db.session.commit()
        return schedule_instance

    def get_lesson(self, lesson_number: int):
        """
        Get a lesson from the day schedule by its number\n
        :param lesson_number: number of the lesson to get from the day schedule
        """
        if lesson_number == 1:
            return self.first_lesson
        elif lesson_number == 2:
            return self.second_lesson
        elif lesson_number == 3:
            return self.third_lesson
        elif lesson_number == 4:
            return self.fourth_lesson
        elif lesson_number == 5:
            return self.fifth_lesson
        else:
            return "Invalid lesson number"
