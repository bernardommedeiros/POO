print ("Digite a base e altura do triangulo:")
b = float(input())
a = float(input())

area = b * a
perimetro = (b+a) * 2
diagonal = (b**2 + a**2) **0.5

print (f"{area:.2f}", f"{perimetro:.2f}", f"{diagonal:.2f}")