from math import sqrt
x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())

distancia = ((((x2 - x1)**0.5) + ((y2 - y1)** 0.5)))

print (f"{distancia:2f}")