soma: float = (lambda num: (sum((1/i for i in range(1, 101)))))([n for n in range(101)])
print(f"Soma: {soma}")
