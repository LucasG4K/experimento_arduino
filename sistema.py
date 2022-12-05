from class_arduino import *
from class_Joule import *
from class_analise import *
from class_interface import*

def parser(value):
    try:
        return float(value)
    except ValueError:
        return

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

    # GUI LOOP
    graph = janela['Graph']
    plt.ioff()                          # Turn the interactive mode off
    fig = plt.figure(1)                 # Create a new figure
    pack_figure(graph, fig)           # Pack figure under graph
    controle = False

    while True:
        event, values = janela.read(timeout=10)       
# =====================================================================
        #quando a janela for fechada
        if event == sg.WIN_CLOSED:
            break
# =====================================================================
        #ir para a próxima janela
        elif event == 'Confirmar':
            # PARÂMETROS DADOS PELO USUÁRIO -> IMPLEMENTAR NA INTERFACE
            joule.set_resistor(parser(values['resistencia']))
            joule.set_cap_term_recipiente(parser(values['C_reserv']))
            joule.set_massa_fluido(parser(values['m_fluido']))
            t_max = parser(values['t_max'])
            if controle == False: controle = init = True
# =====================================================================
        elif event == 'Parar':
            controle = init = False
# =====================================================================
        elif event == sg.TIMEOUT_EVENT and controle == True:
# =====================================================================
        # FLUSH SERIAL e ARQUIVO
            temp = data.getSensorData()
            if init == True:
                data.clear_serial()
                temp = data.getSensorData()
                analise.novoArquivo()
                joule.set_T0 = temp[0]
                joule.set_t0()
                print(joule.get_dt())
                init = False
# =====================================================================
            # INICIA EXPERIMENTO
            if init == False and joule.get_dt() < t_max:
                analise.att_arquivo(joule.get_dt(), temp[0])
                analise.plot(t_max)
            else: 
                print(analise.coef())
                controle = False
# =====================================================================
    janela.close()
