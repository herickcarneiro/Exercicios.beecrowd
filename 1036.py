import math

a,b,c = map(float, input().split())

if b*b-4*a*c < 0:
    print('Impossivel calcular')
elif a == 0:
    print('Impossivel calcular')
else:
    d = b**2-4*a*c
    rd = math.sqrt(d)
    r1 = (-b+rd)/(2*a)
    r2 = (-b-rd)/(2*a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))