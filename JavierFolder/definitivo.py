from pynfc import Nfc, Timeout
import time

pn532 = Nfc("pn532_uart:/dev/ttyS0")
for target in pn532.poll():
    try:
         if target is None:
             break 
         else:
             print('ID: ' +target.uid.decode('ascii').upper()+'\n')
    except TimeoutException:
        pass



