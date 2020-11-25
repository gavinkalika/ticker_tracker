from datetime import datetime
from app.DateTimeValueObject import DateTimeValueObject


class LogEntity():

    def __init__(self):
        self.created_date = DateTimeValueObject()
