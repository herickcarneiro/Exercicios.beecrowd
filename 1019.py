n = int(input())
h = n//3600
n = n-(h*3600)
m = n//60
n = n-(m*60)
s = n

print(f'{h}:{m}:{s}')