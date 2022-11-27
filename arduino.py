from pyfirmata import Arduino, util
from numpy import polyfit
from pandas import read_csv
from time import sleep
import csv

def analog_conv(valor):
    return (valor * 5000 - 500) / 10

# prefixo -> info_: valor do sensor
# fórmula a ser tratada: T(t) = V*i*t/C + To => C * (T - To) = V*i*t => C = V*i*t / (T - To)

if __name__ == '__main__':
    board = Arduino('COM3')
    iterator = util.Iterator(board)
    try:
        iterator.start()
    except:
        print('Erro ao inicializar')

#------------------------------------------
# VARIÁVEIS
    timer          = 0
    intervalo      = 0.5 # PODE ser definido pelo usuário
    resistor    = 10.4 # definido pelo usuário
    C_reservatorio = 20 # definido pelo usuário
    tempo_maximo   = 30 # definido pelo usuário
    file           = 'data.csv'
    fieldname      = ['tempo', 'temperatura']
    temperatura    = board.get_pin('a:0:i')
    tensao         = board.get_pin('a:1:i')
    sleep(0.2)
    temperatura_inicial = temperatura.read()
#------------------------------------------
# ABERTURA DO ARQUIVO
    with open(file, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
        csv_writer.writeheader()
#------------------------------------------
# dT DEVE SER DIFERENTE DE 0 PARA INICIAR
    print('começando')
    while temperatura.read() - temperatura_inicial == 0:
        sleep(1)
#------------------------------------------
# LOOP DO PROGRAMA
    while timer < tempo_maximo:
        info_temperatura = temperatura.read() * 30 + 20 # temperatura.read()
        info_tensao = tensao.read() * 20

        if info_temperatura - temperatura_inicial != 0:
            C_linha = info_tensao**2/resistor * timer / (info_temperatura - temperatura_inicial)

        data = read_csv(file)
        if len(data[fieldname[0]]) > 1:
            coef = polyfit(data[fieldname[0]], data[fieldname[1]], 1)
            print(coef)

        with open(file, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
            info = {fieldname[0]: round(timer,2), fieldname[1]: info_temperatura}
            csv_writer.writerow(info)

        print(round(timer,2), info_temperatura, info_tensao)
        # print(C)

        sleep(intervalo)
        timer += intervalo

    C = (info_temperatura*info_tensao - C_reservatorio) / coef[0]
    print(C)
