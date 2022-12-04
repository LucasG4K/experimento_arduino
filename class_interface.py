
from PySimpleGUI import PySimpleGUI as sg

def inicializa(J, R, M, CR):
    J.set_resistor(R)
    J.set_massa_fluido(M)
    J.set_cap_term_recipiente(CR)

def parser(value):
    try:
        return float(value)
    except ValueError:
        return

#janela de dados
def janelaDados():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Dados                                ')],
        [sg.Text('Tempo de análise(s)                  '), sg.Input(key = 't_max', size = (10,1))],
        [sg.Text('Resistência(ohm)                      '), sg.Input(key = 'resistencia', size = (10,1))],
        [sg.Text('Cap. Térmica Reservatório (J/ºC)'), sg.Input(key = 'Capacidade_reservatorio', size = (10,1))],
        [sg.Text('Massa do fluido(Kg)                  '), sg.Input(key = 'massa_fluido', size = (10,1))],
        [sg.Button('Confirmar')]
    ]
    return sg.Window('Dados',  layout = layout, finalize= True)

def janelaAtulaizacaoDados():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Atualização em tempo real')],
        [sg.Text('', key = 'Temperatura')],
        [sg.Text('', key = 'Tempo')],
        [sg.Text('', key = 'Ax+B')],
        [sg.Button('Plotar grafico'), sg.Button('Voltar')]
    ]
    return sg.Window('Atualização dos dados', layout = layout, finalize= True)
