from class_arduino import *
from class_Joule import *
from class_analise import *
from time import sleep

def init_exp():
    pass

if __name__ == '__main__':
# =====================================================================
    # INICIA CONFIG ARDUINO
    serial_port = 'COM5'
    arduino = arduino(serial_port)

    arduino.cria_porta() # definida entrada 0
    sleep(.05)
# =====================================================================
    # PARÂMETROS DADOS PELO USUÁRIO -> IMPLEMENTAR NA INTERFACE
    R = float(input('Entre com o valor do resistor (ohm):')) # resistor para aquecimento => PARAM. OBRIGATÓRIO
    massa_fluido = float(input('Entre com o valor da massa de fluido (Kg): ')) # => PARAM. OBRIGATÓRIO
    C_recipiente = float(input('Entre com o valor da capacidade térmica (J/°C)')) # => PARAM. NÃO OBRIGATÓRIO
# =====================================================================
    # INICIA CONFIG JOULE
    joule = Joule(R, massa_fluido, C_recipiente)
# ====================================================================
    # INTERFACE GRÁFICA EM LOOP DEVE FICAR AQUI
