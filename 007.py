tinta_caneta: float = float(input("Quantidade de tinta da caneta: "))
tinta_original: float = tinta_caneta

desconto:float = tinta_original / 50

while tinta_caneta > 0:
    print("Enquanto tem tina a caneta escreve " + str(tinta_caneta))

    tinta_caneta -= desconto
