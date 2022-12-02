from numpy import polyfit

class Analise:
    # def __init__(self):
    #     pass

    def coef(_,x,y):
        return polyfit(x, y, 1)