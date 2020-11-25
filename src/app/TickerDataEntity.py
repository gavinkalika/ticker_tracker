from datetime import datetime
from app.DateTimeValueObject import DateTimeValueObject


class TickerDataEntity:

    def __init__(self, rank, close, dollar_change, percentage_change, volumne, tsi, last_insert_id, id=None):
        self.tsi = tsi

        self.percentage_change = percentage_change.strip('-')
        self.percentage_change = self.percentage_change.strip('%')
        self.percentage_change = float(self.percentage_change)
        self.percentage_change = '{:.2f}'.format(self.percentage_change / 100)

        self.dollar_change = dollar_change.strip('-')
        self.dollar_change = self.dollar_change.strip('$')
        self.dollar_change = float(self.dollar_change)
        self.close = close
        self.volume = volumne
        self.rank = rank
        self.id = id
        self.last_insert_id = last_insert_id
        self.created_date = DateTimeValueObject()

    def get_list(self):
        return [self.rank, self.close, self.dollar_change, self.percentage_change, self.volume, self.tsi, self.last_insert_id, self.created_date.db_format()]
