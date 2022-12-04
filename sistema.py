from class_arduino import *
from class_Joule import *
from class_analise import *
from class_interface import*

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
    
    #Criando Janelas iniciais
    janela1, janela2 = janelaDados(), None

    while True:
        window,event,values = sg.read_all_windows()
        
        
        
        #quando a janela for fechada
        if window == janela1 and event == sg.WIN_CLOSED:
            break
        #ir para a próxima janela
        if window == janela1 and event == 'Confirmar':
            joule.set_resistor(parser(values['resistencia']))
            joule.set_cap_term_recipiente(parser(values['Capacidade_reservatorio']))
            joule.set_massa_fluido(parser(values['massa_fluido']))
            t_max = parser(values['t_max'])
            janela2 = janelaAtulaizacaoDados()
            janela1.hide()

        if window == janela2 and event == 'Plotar grafico':
# =====================================================================
        # FLUSH SERIAL e ARQUIVO
            analise.novoArquivo()
            data.clear_serial()
            temp = data.getSensorData()
            # INICIA EXPERIMENTO

            joule.set_T0 = temp[0]
            joule.set_t0()
            
            while joule.get_dt() < t_max:
                a = joule.capacidade_termica(temp[1],joule.resistor,temp[0])
                b = joule.calor_especifico(a)
                # print('EM TEMPO REAL: C='+ str(a) + 'J/°C c = ' + str(b) + 'J/Kg°C')
                analise.att_arquivo(joule.get_dt(), temp[0])
                analise.plot()
                sleep(1)
                temp = data.getSensorData()
                janela2['Temperatura'].update(f'T(t)={temp[0]} °C')
                janela2['Tempo'].update(f't={joule.get_dt()} s')
            
            janela2['Ax+B'].update(f'{analise.coef()[0]}t + {analise.coef()[1]}')
        
        if window == janela2 and event == 'Voltar':
            janela2.hide()
            janela1.un_hide()
        if window == janela2 and event ==  sg.WIN_CLOSED:
            break