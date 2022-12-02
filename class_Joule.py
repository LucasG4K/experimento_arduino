from datetime import datetime
class Joule:

    def __init__(self, resistor,massa_fluido = 0.0,cap_term_recipiente = 0.0):
        self.resistor = resistor
        self.massa_fluido = massa_fluido
        self.cap_term_recipiente = cap_term_recipiente
        self.T0 = 0

    def set_T0(self, temperature):
        self.T0 = temperature
    
    def set_t0(self):
        self.t0 = datetime.now()

    def get_dt(self):
        return datetime.now()

    def get_temperature(voltage_value): # converte a tensao do sensor em temperatura
        pass
    
    def get_voltage(voltage_value): # converte a tensao do sensor em tensao saída da fonte
        return voltage_value * 5 # x5 para converter em saída ou 7250 / (72500 + 29700)
        
    def capacidade_termica(self, V,R,t,T): # para chamar (voltage(volts), resistor,time, temperature(T)
        if R > 0 and T - self.t0 != 0:
            return (V**2 / R) * t / (T - self.t0) - self.cap_term_recipiente # J/s / °C ou J/°C
        else: return 0

    def calor_especifico(self, cap_term_fluido):
        if self.massa_fluido > 0:
            return cap_term_fluido / self.massa_fluido
        else: return 0
