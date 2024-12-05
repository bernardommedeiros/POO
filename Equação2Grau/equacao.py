class Equacao:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    if a == 0: raise ValueError ("Coeficiente a inválido")
        
    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    def x1(self):
        return (-self.__b + math.sqrt(self.delta()))
    def x1(self):
        if self.delta() >= 0:
         return (-self.__b + math.sqrt(self.delta()))
    def x1(self):
        return (-self.__b + math.sqrt(self.delta()))

eq = Equacao(1, 0, -4)
print(eq.delta())
print(eq.delta)
