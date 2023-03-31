import sqlite3
import time
import datetime
from time import sleep
import serial

#BinaryIO
#IOBase


conn = sqlite3.connect("Data.db", check_same_thread = False )
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Solpanel(unix REAL, Date TEXT, Y REAL)') 


def data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    y = mAhData
    c.execute("INSERT INTO Solpanel (unix, Date, Y) VALUES (?, ?, ?)",
              (unix, date, y))
    conn.commit()

while True:
    ser = serial.Serial('/dev/ttyS0', 115200, timeout=5)
    data = ser.readline()
    if data:
        #print(data.decode().strip())
        mAhData = int(data.decode().strip())
        print(mAhData)
    
    create_table()
    data_entry()
    sleep(0.5)
