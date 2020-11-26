# from package import specific_submodule
import mysql.connector
from mysql.connector import Error
from app.TickerDataEntity import TickerDataEntity
from app.TickerEntity import TickerEntity
from app.TickerStmts import insert_ticker_data_stmt, insert_ticker_stmt, insert_log_stmt, dupe_check_stmt, get_ticker_data_stmt
from app.DateTimeValueObject import DateTimeValueObject


class TickerRepository:
  
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(host='localhost',
                                          database='macro_ops',
                                          user='root',
                                          password='password')
            self.db_conn.autocommit = False
        except Error as error:
            print("Error connecting to MySQL", error)

    def duplicate_check(self):
        """Returns boolean

        Returns:
            [boolean]
        """
        is_dupe = False

        date = DateTimeValueObject()
        self.cursor = self.db_conn.cursor()
        self.cursor.execute(dupe_check_stmt(), [date.db_date_format()])
        result = self.cursor.fetchone()
        is_dupe = len(result) > 0 if type(result) is tuple else False

        return is_dupe

    def save_all(self, data_set):
        """Saves all the ticker data

        Args:
            data_set ([array])
        """
        self.log_data('Start save process.')
        if self.duplicate_check():
            self.log_data('Data already exists in DB - skip save operations')
            return

        self.cursor = self.db_conn.cursor()
        try:

            for row in data_set:
                self.__save_ticker(row)

            self.__save_log()
            self.db_conn.commit()
        except Error as e:
            print('Save error')
            print(e.__str__)
            self.db_conn.rollback()
            self.log_data(e.__str__)
            raise e
        finally:
            self.log_data('Update ticker data successfully.')

    def log_data(self, msg):
        """

        Args:
            msg ([type]): [description]
        """
        msg = [DateTimeValueObject().db_format(), msg]
        f = open('src/log/log.txt', "a")
        f.write("{0} -- {1}\n".format(*msg))

    def __save_ticker_data(self, row, ticker_id):
        """Saves meta data on ticker

        Args:
            row ([array])

        Returns:
            None
        """
        data = TickerDataEntity(row[2], *row[4:], ticker_id)
        data = data.get_list()
        self.cursor.execute(insert_ticker_data_stmt(), data)

    def __save_ticker(self, row):
        """Saves the base ticker data.

        Args:
            row [array]
            last_insert_id [integer]
        """

        data = TickerEntity(row[3])
        ticker_exists = self.__get_existing_ticker(ticker=data.ticker_id)

        if ticker_exists is not None:
            self.__save_ticker_data(row, ticker_id=ticker_exists[0])
        else:
            self.cursor.execute(insert_ticker_stmt(), data.get_list())
            self.__save_ticker_data(row, ticker_id=self.cursor.lastrowid)

    def __save_log(self):
        """Update insert log

            Returns:
                [None]
        """
        dt = DateTimeValueObject()
        self.cursor.execute(insert_log_stmt(), [dt.db_date_format(), dt.db_time_format()])

    def __get_existing_ticker(self, ticker):
        self.cursor.execute(get_ticker_data_stmt(), [ticker])
        return self.cursor.fetchone()
