

import os
import TSYS01
import time
import datetime

sensor=TSYS01.TSYS01(0x77)

while True:    
    time.sleep(5)
    os.system("clear")
    temperature  = sensor.readTemp()
    timeStr = str(datetime.datetime.now())
    temperatureString   = timeStr + ";" + str(temperature) +  "\r\n"
    with open('log','a') as f:
        f.write (temperatureString)
    print 'Temperature = %3.3f C' % temperature
    

