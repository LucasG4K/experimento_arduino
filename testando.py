from pyfirmata import Arduino, util
from time import sleep

try:
    board = Arduino('COM4')
    iterator = util.Iterator(board)
    iterator.start()
except:
    print('Erro ao inicializar.')

t = board.get_pin('a:0:i')
sleep(.05)
print(t.read()*5)