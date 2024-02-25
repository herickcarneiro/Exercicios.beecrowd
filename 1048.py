n = float(input())

if n>0 and n<=400.0:
    print("Novo salario: {:.2f}".format(n*1.15))
    print("Reajuste ganho: {:.2f}".format(n*0.15))
    print(f"Em percentual: 15 %")
elif n>400.0 and n<=800.0:
    print("Novo salario: {:.2f}".format(n*1.12))
    print("Reajuste ganho: {:.2f}".format(n*0.12))
    print(f"Em percentual: 12 %")
elif n>800.0 and n<=1200.0:
    print("Novo salario: {:.2f}".format(n*1.10))
    print("Reajuste ganho: {:.2f}".format(n*0.10))
    print(f"Em percentual: 10 %")
elif n>1200.0 and n<=2000.0:
    print("Novo salario: {:.2f}".format(n*1.07))
    print("Reajuste ganho: {:.2f}".format(n*0.07))
    print(f"Em percentual: 7 %")
else:
    print("Novo salario: {:.2f}".format(n*1.04))
    print("Reajuste ganho: {:.2f}".format(n*0.04))
    print(f"Em percentual: 4 %")
    