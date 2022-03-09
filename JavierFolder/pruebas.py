from Rfid import Rfid
rf=Rfid()
uid=rf.read_uid()
print(uid)