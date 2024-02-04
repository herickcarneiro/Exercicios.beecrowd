a,b,c = map(int, input().split())

if a > b:
    maiorAB = a
else:
    maiorAB = b

if maiorAB > c:
    print(f'{maiorAB} eh o maior')
else:
    print(f'{c} eh o maior')