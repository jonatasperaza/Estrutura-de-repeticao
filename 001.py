minha_lista: list = []

for _ in range(20):
    numero =input("Digite um número inteiro: ")
    if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
        numero = int(numero)
    else:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue
    minha_lista.append(numero)

print(f"Numero negativos na lista: {[num for num in minha_lista if num < 0]}")
print(f"Média dos numeros positivos na lista: {(sum([num for num in minha_lista if num > 0]) / len([num for num in minha_lista if num > 0])):.2f}")
