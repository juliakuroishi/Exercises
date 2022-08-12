a = float(input('Digite a'))
b = float(input('Digite b'))
c = float(input('Digite c'))

import math

delta = ((b**2) -4 * (a * c))

if delta > 0:
    x1 = (-b + math.sqrt (delta)) / (2 * a) 
    x2 = (-b - math.sqrt (delta)) / (2 * a) 
    print ('as raízes da equação são ')
    if x1<x2:
        print (x1, 'e', x2)
    else:
        print (x2, 'e', x1)

elif delta == 0:
    x = (-b + math.sqrt (delta)) / (2 * a)
    print ('a raiz desta equação é ', x)

else: 
    print ('esta equação não possui raízes reais')