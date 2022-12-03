import serial.tools.list_ports

class Arduino:
    def INCERTEZA_INSTRUMENTO(value): return value * 0.03

    def __init__(self):
        ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()

        portsList = []

        for onePort in ports:
            portsList.append(str(onePort))
            print(str(onePort))

        val = input("Select Port: COM")

        for x in range(0,len(portsList)):
            if portsList[x].startswith("COM" + str(val)):
                portVar = "COM" + str(val)
                print(portVar)

        try:
            self.serialInst.baudrate = 9600
            self.serialInst.port = portVar
            self.serialInst.open()
        except:
            print('Erro ao inicializar.')

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