from numpy import polyfit, poly1d, linspace
from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    data = read_csv('data.csv')
    x = data['tempo']
    y = data['temperatura']

    plt.cla()
    plt.ylabel('Temperatura (°C)')
    plt.xlabel('Tempo (s)')

    if len(x) > 1:
        coef = polyfit(x,y,1)
        poly1d_fn = poly1d(coef)
        plt.plot(x, y, '.', x, poly1d_fn(x), '--')
        print('A = ' + str(coef[0]) + '; B = ' + str(coef[1]))
    else: plt.scatter(x,y)
    
    plt.legend(['Temperatura', 'Ajuste Linear'], loc='upper left')
    # plt.text('A = ' + str(coef[0]), 'B = ' + str(coef[1]))
    plt.tight_layout()


# if __name__ == '__main__':
# def grafico():
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()