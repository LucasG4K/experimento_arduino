import requests
from tkinter import *
# import plot
import arduino

intervalo = 0
resistor = 0
C_reservatorio = 0
tempo_maximo = 0
massa_fluido = -1

janela = Tk()
janela.title("Teste")
janela.geometry('500x500')
texto = Label(janela, text="Informe os valores", font=('Arial 10'), anchor= 'w')
texto.grid(column=0, row=0, padx=10, pady=10, sticky=NSEW)

def parser(value):
    try:
        return float(value)
    except ValueError:
        return 0

def obter():
    intervalo = parser(entry_enttempo.get())
    resistor = parser(entry_resist.get())
    C_reservatorio = parser(entry_creserv.get())
    tempo_maximo = parser(entry_tmax.get())
    massa_fluido = parser(entry_massflui.get())
    print(intervalo, resistor, C_reservatorio, tempo_maximo, massa_fluido)
    arduino.main(intervalo, resistor, C_reservatorio, tempo_maximo, massa_fluido)

texto1 = Label(janela, text="Intervalo de Tempo:", font=('Arial 10'), anchor= 'w')
texto1.grid(column=0, row=2, padx=10, pady=10, sticky=NSEW)
entry_enttempo = Entry(janela, width=10, font=('Arial 10'))
entry_enttempo.grid(column= 1,row =2, padx=10, pady=10 )

texto2 = Label(janela, text="Resistência:", font=('Arial 10'), anchor= 'w')
texto2.grid(column=0, row=3, padx=10, pady=10, sticky=NSEW)
entry_resist = Entry(janela, width=10, font=('Arial 10'))
entry_resist.grid(column= 1,row =3, padx=10, pady=10 )

texto3 = Label(janela, text="Capacidade do Reservatório:", font=('Arial 10'), anchor= 'w')
texto3.grid(column=0, row=4, padx=10, pady=10, sticky=NSEW)
entry_creserv = Entry(janela, width=10, font=('Arial 10'))
entry_creserv.grid(column= 1,row =4, padx=10, pady=10 )

texto4 = Label(janela, text="Tempo máximo:", font=('Arial 10'), anchor= 'w')
texto4.grid(column=0, row=5, padx=10, pady=10, sticky=NSEW)
entry_tmax = Entry(janela, width=10, font=('Arial 10'))
entry_tmax.grid(column= 1,row =5, padx=10, pady=10 )

texto5 = Label(janela, text="Massa do fluído:", font=('Arial 10'), anchor= 'w')
texto5.grid(column=0, row=6, padx=10, pady=10, sticky=NSEW)
entry_massflui = Entry(janela, width=10, font=('Arial 10'))
entry_massflui.grid(column= 1,row =6, padx=10, pady=10 )

botao = Button(janela, text="Confirmar", command =lambda: obter())
botao.grid(column=0, row=7, padx=10, pady=10)
botao = Button(janela, text="Exibir Gráfico", command =lambda: print('init()'))
botao.grid(column=0, row=8, padx=10, pady=10)


janela.mainloop()