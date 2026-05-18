# 100/0! + 99/1! + 98/2! + ... + 80/20!
#
#

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(sum((100 - i) / fatorial(i) for i in range(21)))
