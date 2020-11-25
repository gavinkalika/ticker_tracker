import requests
import pandas as pd
from app.TickerRepository import TickerRepository
import schedule
import time


def job():
    """[summary]
    """

    url = None
    with open('ticker_tracker/fileUrl/fileUrl.txt') as fileReader:
        url = fileReader.read()

    r = requests.get(url)
    data = r.content
    repo = TickerRepository()

    try: 
        list = pd.read_html(data)
    except:  # catch all error
        repo.log_data('Unable to fetch data from from google docs')

    dataFrame = list.pop(0)

    list = dataFrame.values.tolist()
    list.pop(0)

    data_to_save = []
    for i, row in enumerate(list, start=0):
        if i == 0:
            continue
        data_to_save.append(row)

    repo.save_all(data_set=data_to_save)


if __name__ == '__main__':
    schedule.every().monday.at("20:00").do(job)
    schedule.every().tuesday.at("20:00").do(job)
    schedule.every().wednesday.at("20:00").do(job)
    schedule.every().thursday.at("20:00").do(job)
    schedule.every().friday.at("20:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(3600)



# https://pypi.org/project/schedule/
# new a python start up script when I      launch computer