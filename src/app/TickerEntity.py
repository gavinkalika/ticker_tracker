from datetime import datetime
from app.DateTimeValueObject import DateTimeValueObject


class TickerEntity:

    def __init__(self, ticker_id, id=None):
        self.ticker_id = ticker_id
        self.id = id
        self.created_date = DateTimeValueObject()

    def get_list(self): 
        return [self.ticker_id, self.created_date.db_format()]
