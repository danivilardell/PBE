import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)
reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)

pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
pn532.SAM_configuration()

print("Esperant targeta NFC...")
if __name__ == "__main__":
    uid = pn532.read_passive_target(timeout=10)
       
    print("UID:", [hex(i) for i in uid])