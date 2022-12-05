from numpy import polyfit, poly1d
from pandas import read_csv
from matplotlib import use as use_agg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg

def pack_figure(graph, figure):
    canvas = FigureCanvasTkAgg(figure, graph.Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side='top', fill='both', expand=1)
    return plot_widget

def plot_figure(t):
    data = read_csv('data.csv')
    x = data['tempo']
    y = data['temperatura']
    fig = plt.figure(1)
    plt.cla()
    plt.legend(['Temperatura', 'Ajuste Linear'], loc='upper left')
    plt.ylabel('Temperatura (°C)')
    plt.xlabel('Tempo (s)')
    plt.title('Temperatura (°C) x tempo (s)')
    plt.axis([-1, t + 1, 10, 60])
    plt.grid()
    plt.tight_layout()

    if len(x) > 1:
        coef = polyfit(x,y,1)
        poly1d_fn = poly1d(coef)
        plt.plot(x, y, '.', x, poly1d_fn(x), '--')
    else: plt.scatter(x,y)
    fig.canvas.draw()

# Use Tkinter Agg
use_agg('TkAgg')

layout = [[sg.Graph((640, 480), (0, 0), (640, 480), key='Graph1')]]
window = sg.Window('Matplotlib', layout, finalize=True)


# Initial
graph1 = window['Graph1']
plt.ioff()                          # Turn the interactive mode off
fig1 = plt.figure(1)                # Create a new figure
ax1 = plt.subplot(111)              # Add a subplot to the current figure.
pack_figure(graph1, fig1)           # Pack figure under graph
plot_figure(10)

while True:

    event, values = window.read(timeout=10)

    if event == sg.WINDOW_CLOSED:
        break
    elif event == sg.TIMEOUT_EVENT:
        plot_figure(10)

window.close()