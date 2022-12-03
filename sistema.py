from class_arduino import *
from class_Joule import *
from class_analise import *

if __name__ == '__main__':
# =====================================================================
    # PARÂMETROS DADOS PELO USUÁRIO -> IMPLEMENTAR NA INTERFACE
    R = float(input('Entre com o valor do resistor (ohm):')) # resistor para aquecimento => PARAM. OBRIGATÓRIO
    massa_fluido = float(input('Entre com o valor da massa de fluido (Kg): ')) # => PARAM. OBRIGATÓRIO
    C_recipiente = float(input('Entre com o valor da capacidade térmica (J/°C: )')) # => PARAM. NÃO OBRIGATÓRIO
    # t_max = int(input('Entre com o valor de tempo máximo de medição: )')) # => PARAM. OBRIGATÓRIO
# =====================================================================
    # INICIA CONFIG CSV
    analise = Analise()
# =====================================================================
    # INICIA CONFIG JOULE
    joule = Joule(R, massa_fluido, C_recipiente)
# =====================================================================
    # INICIA CONFIG ARDUINO
    data = Arduino()
    data.clear_serial()
    temp = data.getSensorData()
# =====================================================================
    # INICIA EXPERIMENTO

    joule.set_T0 = temp[0]
    joule.set_t0()

    while joule.get_dt() < 15:
        a = joule.capacidade_termica(temp[1],R,temp[0])
        b = joule.calor_especifico(a)
        # print('EM TEMPO REAL: C='+ str(a) + 'J/°C c = ' + str(b) + 'J/Kg°C')
        analise.att_arquivo(joule.get_dt(), temp[0])
        analise.plot()
        sleep(5)
        temp = data.getSensorData()

    print(analise.coef())
    analise.show()