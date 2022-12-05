from PySimpleGUI import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import use as use_agg

#interface em pysimple gui
sg.theme('Reddit')
layout = [
    [sg.Text('Dados',                            size=(25, 1))],
    [sg.Text('Tempo de análise(s)',              size=(25, 1)), sg.Input(key = 't_max',       size = (10,1))],
    [sg.Text('Resistência(ohm)',                 size=(25, 1)), sg.Input(key = 'resistencia', size = (10,1))],
    [sg.Text('Cap. Térmica Reservatório (J/°C)', size=(25, 1)), sg.Input(key = 'C_reserv',    size = (10,1))],
    [sg.Text('Massa do fluido(Kg)',              size=(25, 1)), sg.Input(key = 'm_fluido',    size = (10,1))],
    [sg.Button('Confirmar'), sg.Button('Parar')],
    [sg.Text('Att em tempo real')],
    [sg.Graph((640, 480), (0, 0), (640, 480), key='Graph')]
]
janela = sg.Window('Dados', layout, finalize=True)

def pack_figure(graph, figure):
    canvas = FigureCanvasTkAgg(figure, graph.Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side='top', fill='both', expand=1)
    return plot_widget
