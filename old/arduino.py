from pyfirmata import Arduino, util
from numpy import polyfit
from pandas import read_csv
from time import sleep
import csv

# SENSOR PARA MEDIR CALOR ESPECÍFICO DE FLUIDOS UTILIZANDO EFEITO JOULE

# prefixo -> info_: valor do sensor
# fórmula a ser tratada: T(t) = V*i*t/C + To => C * (T - To) = V*i*t => C = V*i*t / (T - To)

def main(intervalo, resistor, C_reservatorio, tempo_maximo, massa_fluido):
    try:
        board = Arduino('COM4')    
        iterator = util.Iterator(board)
        iterator.start()
    except:
        print('Erro ao inicializar')

#------------------------------------------
# VARIÁVEIS
    # intervalo      # PODE ser definido pelo usuário
    # resistor       # definido pelo usuário
    # C_reservatorio # definido pelo usuário
    # tempo_maximo   # definido pelo usuário
    # massa_fluido   # pode ser definido pelo usuário, se < 0 não define calor específico
    timer          = 0
    file           = 'data.csv'
    fieldname      = ['tempo', 'temperatura']
    temperatura    = board.get_pin('a:0:i')
    print(type(temperatura))
    tensao         = board.get_pin('a:1:i')
    R1             = 29500.0 # 29900.0
    R2             = 7000.0  # 7500
    sleep(0.2)
    temperatura_inicial = temperatura.read()
#------------------------------------------
# ABERTURA DO ARQUIVO
    with open(file, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
        csv_writer.writeheader()
#------------------------------------------
# LOOP DO PROGRAMA
    while timer <= tempo_maximo:
        ajuste_temperatura = temperatura.read() * 5 # conversao em volts
        info_temperatura   = ajuste_temperatura
        ajuste_tensao      = tensao.read() * 5 # conversao em volts
        info_tensao        = ajuste_tensao / (7250 / (7250 + 29700))

        # if info_temperatura - temperatura_inicial != 0:
        #     C_linha = info_tensao**2/resistor * timer / (info_temperatura - temperatura_inicial)

        data = read_csv(file)
        if len(data[fieldname[0]]) > 1:
            coef = polyfit(data[fieldname[0]], data[fieldname[1]], 1)
            # print(coef)

        with open(file, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
            info = {fieldname[0]: round(timer,2), fieldname[1]: info_temperatura}
            csv_writer.writerow(info)

        print(round(timer,2), info_temperatura, info_tensao)

        sleep(intervalo)
        timer += intervalo

    C = (info_temperatura*info_tensao - C_reservatorio) / coef[0]
    if float(massa_fluido) > 0:
        c = C/float(massa_fluido)
    else:
        c = 'massa não definida'

    print(C, c)