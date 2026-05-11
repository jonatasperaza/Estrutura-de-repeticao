n: int = int(input("Insira o valor de N: "))
soma: float = (lambda num: (sum((i / n - 1 + 1 for i in range(n)))))(
    [n for n in range(n)]
)
print(f"Soma: {soma}")
