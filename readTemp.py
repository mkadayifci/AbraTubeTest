# Qucik test file to open TSY01 connection and reads its temp
# 20160819 IMD
#
#

import os
import TSYS01
import time

sensor=TSYS01.TSYS01(0x77)

while True:    
    time.sleep(1)
    os.system("clear")
    temperature  = sensor.readTemp()
    temperatureString   = str(temperature) + "\r\n"
    with open('log','a') as f:
        f.write (temperatureString)
    print 'Temperature = %3.3f C' % temperature
    

