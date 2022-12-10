from datetime import datetime
class Joule:

    def __init__(self, resistor = 1.0, massa_fluido = 0.0, cap_term_recipiente = 0.0):
        self.resistor = resistor
        self.massa_fluido = massa_fluido
        self.cap_term_recipiente = cap_term_recipiente
        self.cap_term_estimada = 0
        self.cal_esp_estimada = 0
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

# -------------------------------------------------------------------------------------------
    # VALORES ESTIMADOS
    def cap_term_estimado(self,pot,coef):
        self.cap_term_estimada = pot/coef[0] - self.cap_term_recipiente

    def cal_esp_estimado(self):
        self.cal_esp_estimada = self.cap_term_estimada / self.massa_fluido
# -------------------------------------------------------------------------------------------

    
