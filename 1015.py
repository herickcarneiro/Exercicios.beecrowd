import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

d = (x2-x1)**2 + (y2-y1)**2
d = math.sqrt(d)

print('{:.4f}'.format(d))