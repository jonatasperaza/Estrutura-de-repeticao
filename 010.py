def fatorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(f"Fatorial: {fatorial(int(input('Insira um número para calcular o fatorial: ')))}")
