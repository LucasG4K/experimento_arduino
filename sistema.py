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
            janela['status'].update('Encerrado!')
            sg.Popup(f'A = {analise.coef()[0]}\nB = {analise.coef()[1]}\nCapacidade térmica estimada = {joule.cap_term_estimada} J/°C\nCalor específico estimado = {joule.cal_esp_estimada} J/Kg°C\nTemperatura inicial estimada = {round(analise.coef()[1], 4)} °C', keep_on_top = True)
# =====================================================================
        elif event == sg.TIMEOUT_EVENT and controle == True:
# =====================================================================
            janela['status'].update('Executando...')
            # INICIA EXPERIMENTO
            if init == False and joule.get_dt() < t_max:
                # COLETA
                temp = data.getSensorData()

                # ESTIMATIVAS
                joule.cap_term_estimado(temp[1]**2/joule.resistor, analise.coef())
                joule.cal_esp_estimado()
                
                # ARQUIVO
                analise.att_arquivo([joule.get_dt(), temp[0], temp[1]**2 / joule.resistor, joule.cap_term_estimada, joule.cal_esp_estimada, analise.coef()[0], analise.coef()[1]])
                analise.plot(t_max)
            elif init == True:
                # INICIALIZA
                analise.novoArquivo()
                temp = data.getSensorData()
                joule.set_T0 = temp
                joule.set_t0()

                # ARQUIVO
                analise.att_arquivo([joule.get_dt(), temp[0], temp[1]**2 / joule.resistor, joule.cap_term_estimada, joule.cal_esp_estimada, analise.coef()[0], analise.coef()[1]])
                analise.plot(t_max)
                init = False
# =====================================================================
            # CONTINUA EXPERIMENTO
            else:
                print(analise.coef())
                controle = False
                janela['status'].update(f'Finalizado!')
                sg.Popup(f'A = {analise.coef()[0]}\nB = {analise.coef()[1]}\nCapacidade térmica estimada = {joule.cap_term_estimada} J/°C\nCalor específico estimado = {joule.cal_esp_estimada} J/Kg°C\nTemperatura inicial estimada = {round(analise.coef()[1], 4)} °C', keep_on_top = True)
            print('--------\n'+ str(temp) + '\n------------')
# =====================================================================
    janela.close()
