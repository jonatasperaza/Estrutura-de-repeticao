canais = [4, 5, 9, 12]
n = 3

ncanais: list[int] = []
npessoas: list[int] = []

for _ in range(n):
    canal = int(input("Digite o canal: "))
    pessoa = int(input("Digite a quantidade de pessoas: "))

    if canal in canais:
        ncanais.append(canal)
        npessoas.append(pessoa)

altura = max(npessoas)

largura = len(ncanais) * 4 + 1

print("#" * largura)

for nivel in range(altura, 0, -1):
    linha = "#"

    for pessoas in npessoas:
        if pessoas >= nivel:
            linha += " * "
        else:
            linha += "   "

    linha += " #"
    print(linha)

linha = "#"

for canal in ncanais:
    linha += f"{canal:>3}"

linha += " #"

print(linha)
print("#" * (largura - 1))
