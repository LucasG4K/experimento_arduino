import serial.tools.list_ports
from time import sleep

class Arduino:
    def INCERTEZA_INSTRUMENTO(value): return value * 0.03

    def __init__(self):
        ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()

        portsList = []

        for onePort in ports:
            portsList.append(str(onePort))
            print(str(onePort))

        for x in portsList:
            print(x[:4] + ' escolhida!')
            if 'COM' in x:
                portVar = str(x[:4])

        while True:
            try:
                self.serialInst.baudrate = 9600
                self.serialInst.port = portVar
                self.serialInst.open()
                break
            except:
                print('Erro ao inicializar.')
                sleep(1)
        
    def clear_serial(self):
        self.serialInst.flush()
    
    def serial(self):
        if self.serialInst.in_waiting: 
            packet = self.serialInst.readline()
            t = str(packet.decode('utf').rstrip('\n')).split(',')
            return t
    
    def getSensorData(self):
        while True:
            try:
                t = self.serial()
                return [float(t[0]), float(t[1])]
            except: pass