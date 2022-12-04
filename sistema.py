from class_arduino import *
from class_Joule import *
from class_analise import *
import requests
from tkinter import *
from PySimpleGUI import PySimpleGUI as sg

# parser(entry_resist.get()), parser(entry_creserv.get()), parser(entry_massflui.get())

def parser(value):
    try:
        return float(value)
    except ValueError:
        return 0

if __name__ == '__main__':

# =====================================================================
    # INICIA CONFIG CSV
    analise = Analise()
# =====================================================================
    # INICIA CONFIG ARDUINO
    data = Arduino()
# =====================================================================
    # INICIA CONFIG JOULE
    joule = Joule()
# =====================================================================
    # PARÂMETROS DADOS PELO USUÁRIO -> IMPLEMENTAR NA INTERFACE

#interface em pysimple gui

#layout
    sg.theme('Reddit')
    layout = [
        [sg.Text('Dados                                '),       sg.Text("                            Atualização em tempo real")],
        [sg.Text('Tempo de análise(s)                  '), sg.Input(key = 't_max', size = (10,1)),       sg.Text("", key = "Temperatura")],
        [sg.Text('Resistência(ohm)                      '), sg.Input(key = 'resistência', size = (10,1)),   sg.Text("", key = "Tempo")],
        [sg.Text('Cap. Térmica Reservatório (J/ºC)'), sg.Input(key = 'Capacidade_reservatorio', size = (10,1)),  sg.Text("", key = "Ax+B")],
        [sg.Text('Massa do fluido(Kg)                  '), sg.Input(key = 'massa_fluido', size = (10,1))],
        [sg.Button('Confirmar')]
    ]
    
    # Janela1
    janela = sg.Window('experimento', layout)
    #ler enventos
    while True:
        eventos, valores = janela.read()
         
        joule.set_resistor(parser(valores["resistência"]))
        joule.set_cap_term_recipiente(parser(valores["Capacidade_reservatorio"]))
        joule.set_massa_fluido(parser(valores["massa_fluido"]))
        

        if eventos == sg.WINDOW_CLOSED:
            break 
        if eventos == 'Confirmar':
#======================================================================
        #Inicializando os valores
        
# =====================================================================
        # FLUSH SERIAL e ARQUIVO
            analise.novoArquivo()
            data.clear_serial()
            temp = data.getSensorData()
# =====================================================================
            # INICIA EXPERIMENTO

            joule.set_T0 = temp[0]
            joule.set_t0()
            
            while joule.get_dt() < parser(valores["t_max"]):
                a = joule.capacidade_termica(temp[1],joule.resistor,temp[0])
                b = joule.calor_especifico(a)
                # print('EM TEMPO REAL: C='+ str(a) + 'J/°C c = ' + str(b) + 'J/Kg°C')
                analise.att_arquivo(joule.get_dt(), temp[0])
                analise.plot()
                sleep(1)
                temp = data.getSensorData()
                janela["Temperatura"].update(f"T(t)={temp[0]} °C")
                janela["Tempo"].update(f"t={joule.get_dt()} s")
            
            janela["Ax+B"].update(f"{analise.coef()[0]}t + {analise.coef()[1]}")
        
            