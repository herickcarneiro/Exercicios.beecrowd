i = int(input())
a = i//365
i = i - (a*365)
m = i//30
i = i - m*30

print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{i} dia(s)')