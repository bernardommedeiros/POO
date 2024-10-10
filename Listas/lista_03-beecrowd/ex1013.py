import math
x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())

distancia = sqrt((((x2 - x1)**2) + ((y2 - y1)**2)))

print (distancia)