from math import prod
# ex = x^0 + x^1/1! + x^2/2! + ... + x^n/n!

ex = (lambda x, n: sum((x**i) / (prod(range(1, i + 1)) or 1) for i in range(n + 1)))(
    1, 30
)

print(ex)
