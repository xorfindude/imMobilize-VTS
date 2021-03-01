import warnings
import serial
import serial.tools.list_ports
from time import sleep

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
# "Dette er den spesifikke porten til min (surface pro 7 - Endre)"
# Kjør koden under for å finne riktig port: 
# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#   print(p)
    if 'USB2.0-Serial' in p.description 
]
if not arduino_ports:
    raise IOError("Culd not find the arduino")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0],115200)
#Liten funksjonstest
sleep(1)
ser.write(b'ir255')
sleep(4)
ser.write(b'ir001')
