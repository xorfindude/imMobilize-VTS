import warnings
import serial
import serial.tools.list_ports
from time import sleep

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'CH3' in p.description
]
if not arduino_ports:
    raise IOError("Culd not find the arduino")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0])
sleep(1)
ser.write(b'ir255')
sleep(4)
ser.write(b'ir001')
