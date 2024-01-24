def fatorial(n):
    fat = 1
    for c in range(n):
        fat *= n
        n -= 1
    return fat


res = fatorial(5)
print(f'O fatorial de 5 é = {res}')


def fatoria(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)


re = fatoria(5)
print(f'o fatorial de 5 é = {re}')
