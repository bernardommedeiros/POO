# objetos == variáveis que carregam o nome da classe

class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
x.b = float(input("informe a base"))
x.h = float(input())

print(f"Area = {x.b*x.h}")