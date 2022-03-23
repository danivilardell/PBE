class Rfid:    
    def read_uid(self):
        from pynfc import Nfc, Timeout
        from time import sleep
        pn532 = Nfc("pn532_uart:/dev/ttyS0")
        for target in pn532.poll():
            try:
                 if target is None:
                     break 
                 else:
                     print('ID: ' +target.uid.decode('ascii').upper()+'\n')
                     sleep(2)
            except TimeoutException:
                pass
        return uid