import serial.tools.list_ports

def PrintComPort():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
    print(p)
