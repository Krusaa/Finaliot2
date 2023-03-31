from time import sleep  
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as gp
import serial
import sqlite3
import time
import datetime


gp.setmode(gp.BCM)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

gp.setup(18,gp.OUT)  
pwm=gp.PWM(18,50)  
pwm.start(0) 

gp.setup(12,gp.OUT)
pwm0=gp.PWM(12,50)
pwm0.start(0)
horiz = 90
verti = 90

pwm.ChangeDutyCycle((verti/18)+2)
pwm0.ChangeDutyCycle((horiz/18)+2)
sleep(1)
pwm.start(0)
pwm0.start(0)

# conn = sqlite3.connect("Data.db", check_same_thread = False )
# c = conn.cursor()


# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS Solpanel(unix REAL, Date TEXT, Y REAL)') 


# def data_entry():
#     unix = time.time()
#     date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#     y = mAhData
#     c.execute("INSERT INTO Solpanel (unix, Date, Y) VALUES (?, ?, ?)",
#               (unix, date, y))
#     conn.commit()



while True:
    # print('LDR VAL0: ', chan0.value)
    # print(verti)
    # print(horiz)
    # print('LDR VAL1', chan1.value)
    # print('LDR VAL2: ', chan2.value)
    # print('LDR VAL3', chan3.value)
 
    # ser = serial.Serial('/dev/ttyS0', 115200, timeout=2)
    # data = ser.readline()
    # if data:
    #     #print(data.decode().strip())
    #     mAhData = int(data.decode().strip())
    #     print(mAhData)

    if chan0.value - 20 > chan1.value and verti > 0:
        verti -= 1
        sig=(verti/18)+2    
        pwm.ChangeDutyCycle(sig)  
        sleep(0.01)
        pwm.start(0)

    if chan1.value - 20 > chan0.value and verti < 180:
        verti += 1
        sig=(verti/18)+2
        pwm.ChangeDutyCycle(sig)
        sleep(0.01)
        pwm.start(0)


    if chan2.value - 20 > chan3.value and horiz < 180:
        horiz += 1
        dig=(horiz/18)+2    
        pwm0.ChangeDutyCycle(dig)  
        sleep(0.01)
        pwm0.start(0)

    if chan3.value - 20 > chan2.value and horiz > 0:
        horiz -= 1
        dig=(horiz/18)+2    
        pwm0.ChangeDutyCycle(dig)  
        sleep(0.01)
        pwm0.start(0)

    # create_table()
    # data_entry()
    # sleep(0.5)

