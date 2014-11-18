import sqlite3
import datetime
import time
import calendar
from datetime import timedelta

date = input("Please enter a date (DD/MM/YYYY): ")
username = input("Please enter a username: ")


def date_to_datetime(date): ## http://stackoverflow.com/questions/17594298/date-time-formats-in-python
    date = datetime.datetime.strptime(date,"%d/%m/%Y")
    return date

def date_to_timestamp(date): ## http://stackoverflow.com/questions/7873828/how-to-convert-date-to-timestamp-using-python
    timestamp = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())
    timestamp_new = timestamp + 86400 ## 86400 on üks ööpäev
    return timestamp, timestamp_new

conn = sqlite3.connect('main.db')
c = conn.cursor()

def print_ts():
    sql = ("SELECT body_xml FROM Messages where chatname is '" + username + "' and timestamp between '%s' and '%s'" % (date_to_timestamp(date)))
    list_sql = []
    for row in c.execute(sql):
        print (row[0])
    conn.close()

if __name__ == '__main__':
    print (print_ts())
