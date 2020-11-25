from datetime import datetime
from datetime import timezone,timedelta

class DateTimeValueObject:

    def __init__(self, tz='UTC') :
        self.date_time = datetime.now(tz=timezone(-timedelta(hours=4)))

    def db_format(self) :
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S")
    
    def db_date_format(self) :
        return self.date_time.strftime("%Y-%m-%d")

    def db_time_format(self) :
        return self.date_time.strftime("%H:%M:%S")