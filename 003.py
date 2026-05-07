conjunto: list = []
while True:
    valor: int = int(input("Digite um número inteiro: "))
    if valor == 0:
        break
    conjunto.append(valor)

print(f"Maior valor: {max(conjunto)}")
print(f"Menor valor: {min(conjunto)}")
