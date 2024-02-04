q, l = map(int, input().split())

match q:
    case 1: x = 4.00
    case 2: x = 4.50
    case 3: x = 5.00
    case 4: x = 2.00
    case 5: x = 1.50

t = l*x
print('Total: R$ {:.2f}'.format(t))