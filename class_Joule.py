from datetime import datetime
class Joule:

    def __init__(self, resistor = 1.0, massa_fluido = 0.0, cap_term_recipiente = 0.0):
        self.resistor = resistor
        self.massa_fluido = massa_fluido
        self.cap_term_recipiente = cap_term_recipiente
        self.T0 = 0
    
    def set_resistor(self, resistor):
        self.resistor = resistor
    
    def set_massa_fluido(self, massa_fluido):
        self.massa_fluido = massa_fluido
    
    def set_cap_term_recipiente(self, cap_term_recipiente):
        self.cap_term_recipiente = cap_term_recipiente

    def set_T0(self, temperature):
        self.T0 = temperature
    
    def set_t0(self):
        self.t0 = datetime.now()

    def get_dt(self):
        return round((datetime.now() - self.t0).total_seconds(),2)
        
    def capacidade_termica(self, TV): # para chamar (voltage(volts), temperature(T)
        if self.resistor > 0 and TV[0] - self.T0 != 0:
            return (TV[1]**2 / self.resistor) * self.get_dt() / (TV[0] - self.T0) - self.cap_term_recipiente # J/s / °C ou J/°C
        else: return 0

    def calor_especifico(self, cap_term_fluido):
        if self.massa_fluido > 0:
            return cap_term_fluido / self.massa_fluido
        else: return 0

    def estima_C(_,pot,coef):
        # At + B
        # A = V*i/C => C = V**2/r*A
        # B = T0
        estimativa = [pot/coef[0] - _.cap_term_recipiente, coef[1]]
        return estimativa

