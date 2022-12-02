from pyfirmata import Arduino, util
from time import sleep

class arduino:
    analog_portas = []
    digital_portas = []

    def __init__(self, serial_port):
        try:
            self.board = Arduino(serial_port)
            iterator = util.Iterator(self.board)
            iterator.start()
        except:
            print('Erro ao inicializar.')
    
    def cria_porta(self):
        if len(self.analog_portas) < 5:
            self.analog_portas.append(self.board.get_pin('a:' + str(len(self.analog_portas)) + ':i'))
            sleep(.05) 
        else:
            print('Erro, portas insuficientes!')
    
    def tensao_porta(self, index): # aciona a porta que deve ser lida -> 0,1,2,3,4 ou 5
        for i in range (0, len(self.analog_portas)):
            if index == i:
                return self.analog_portas[index].read() * 5

