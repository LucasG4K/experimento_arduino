from class_arduino import *
from class_Joule import *
from class_analise import *
import requests
from tkinter import *
# parser(entry_resist.get()), parser(entry_creserv.get()), parser(entry_massflui.get())
def testao(J, R, M, CR):
    J.set_resistor(R)
    J.set_massa_fluido(M)
    J.set_cap_term_recipiente(CR)

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

    janela = Tk()
    janela.title("Teste")
    janela.geometry('500x500')
    texto = Label(janela, text="Informe os valores", font=('Arial 10'), anchor= 'w')
    texto.grid(column=0, row=0, padx=10, pady=10, sticky=NSEW)

    texto1 = Label(janela, text="Tempo máximo:", font=('Arial 10'), anchor= 'w')
    texto1.grid(column=0, row=1, padx=10, pady=10, sticky=NSEW)
    entry_enttempo = Entry(janela, width=10, font=('Arial 10'))
    entry_enttempo.grid(column= 1,row =1, padx=10, pady=10 )

    texto2 = Label(janela, text="Resistência:", font=('Arial 10'), anchor= 'w')
    texto2.grid(column=0, row=2, padx=10, pady=10, sticky=NSEW)
    entry_resist = Entry(janela, width=10, font=('Arial 10'))
    entry_resist.grid(column= 1,row =2, padx=10, pady=10 )

    texto3 = Label(janela, text="Capacidade do Reservatório:", font=('Arial 10'), anchor= 'w')
    texto3.grid(column=0, row=3, padx=10, pady=10, sticky=NSEW)
    entry_creserv = Entry(janela, width=10, font=('Arial 10'))
    entry_creserv.grid(column= 1,row =3, padx=10, pady=10 )

    texto4 = Label(janela, text="Massa do fluído:", font=('Arial 10'), anchor= 'w')
    texto4.grid(column=0, row=4, padx=10, pady=10, sticky=NSEW)
    entry_massflui = Entry(janela, width=10, font=('Arial 10'))
    entry_massflui.grid(column= 1,row =4, padx=10, pady=10 )

    botao = Button(janela, text="Confirmar", command =lambda: testao(joule, parser(entry_resist.get()), parser(entry_creserv.get()), parser(entry_massflui.get())))
    botao.grid(column=0, row=5, padx=10, pady=10)
    botao = Button(janela, text="Exibir Gráfico", command =lambda: print(joule.resistor))
    botao.grid(column=0, row=6, padx=10, pady=10)

    janela.mainloop()
# =====================================================================
    # FLUSH SERIAL

    data.clear_serial()
    temp = data.getSensorData()
# =====================================================================
    # INICIA EXPERIMENTO

    joule.set_T0 = temp[0]
    joule.set_t0()

    while joule.get_dt() < 15:
        a = joule.capacidade_termica(temp[1],joule.resistor,temp[0])
        b = joule.calor_especifico(a)
        # print('EM TEMPO REAL: C='+ str(a) + 'J/°C c = ' + str(b) + 'J/Kg°C')
        analise.att_arquivo(joule.get_dt(), temp[0])
        analise.plot()
        sleep(5)
        temp = data.getSensorData()

    print(analise.coef())
    analise.show()