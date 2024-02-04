n = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]

print(f'{n}')
for dinheiro in cedulas:
    v = n // dinheiro
    n %= dinheiro
    print(f'{v} nota(s) de R$ {dinheiro},00')



