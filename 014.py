soma: float = (lambda num: (num * 32) ** (1/3))(sum(((-1) ** i) / ((2 * i + 1) ** 3)for i in range(51)))

print(f"Soma: {soma}")
