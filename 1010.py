codigo1,quantidade1,valor1 = map(float, input().split())
total1 = quantidade1*valor1

codigo2,quantidade2,valor2 = map(float, input().split())
total2 = quantidade2*valor2

total = total1 + total2

print('VALOR A PAGAR = R$ {:.2f}'.format(total))
