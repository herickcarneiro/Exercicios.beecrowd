a,b,c = map(float, input().split())
pi = 3.14159

area_triangulo = a*c/2
area_circulo = pi*c*c
area_trapezio = (a+b)*c/2
area_quadrado = b*b
area_retangulo = a*b

print("TRIANGULO: {:.3f}".format(area_triangulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapezio))
print("QUADRADO: {:.3f}".format(area_quadrado))
print("RETANGULO: {:.3f}".format(area_retangulo))
