import math

def find_nb(m):
    # find specific number (challenge codewar)
    list = []
    n = m ** (1 / 3)
    for i in range(0, n):
        n = m ** (1/3)
        list.append(n)
    return n

print(find_nb(1986))