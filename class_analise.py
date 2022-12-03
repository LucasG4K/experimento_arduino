from numpy import polyfit, poly1d
from pandas import read_csv
import matplotlib.pyplot as plt
import csv

class Analise:
    nome_arq = 'data.csv'
    cabecalho = ['tempo', 'temperatura']

    def __init__(self):
        with open(self.nome_arq, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.cabecalho)
            csv_writer.writeheader()
    
    def att_arquivo(self,t,T):
        with open(self.nome_arq, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.cabecalho)
            info = {self.cabecalho[0]: t, self.cabecalho[1]: T}
            csv_writer.writerow(info)

    def plot(i):
        data = read_csv('data.csv')
        x = data['tempo']
        y = data['temperatura']

        plt.cla()
        plt.ylabel('Temperatura (°C)')
        plt.xlabel('Tempo (s)')
        plt.axis([0, 500, 10, 40])

        if len(x) > 1:
            coef = polyfit(x,y,1)
            poly1d_fn = poly1d(coef)
            plt.plot(x, y, '.', x, poly1d_fn(x), '--')
            # print('A = ' + str(coef[0]) + '; B = ' + str(coef[1]))
        else: plt.scatter(x,y)
        
        plt.legend(['Temperatura', 'Ajuste Linear'], loc='upper left')
        # plt.text('A = ' + str(coef[0]), 'B = ' + str(coef[1]))
        plt.tight_layout()
        plt.pause(0.05)
    
    def show(_):
        plt.show()

    def coef(_):
        data = read_csv('data.csv')
        x = data['tempo']
        y = data['temperatura']
        return polyfit(x,y,1)