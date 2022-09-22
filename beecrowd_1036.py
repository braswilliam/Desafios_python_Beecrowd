import math
x1 = 0
x2 = 0

entrada = input().split()
a, b, c = entrada
a = float(a)
b = float(b)
c = float(c)

delta = math.pow(b, 2) - (4 * a * c)

if (a != 0) and (delta > 0):
   x1 = ((-b) + math.sqrt(delta)) / (2 * a)
   x2 = ((-b) - math.sqrt(delta)) / (2 * a)
   print(f'R1 = {x1:.5f}')
   print(f'R2 = {x2:.5f}')
else:
    print('Impossivel calcular')

