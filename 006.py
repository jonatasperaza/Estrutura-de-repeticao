valores, negativos = (lambda nums: ([i for i in nums], [i for i in nums if i < 0]))(
    [int(input("Insira um numero: ")) for i in range(20)]
)

print(f"quantidade de valores {len(valores)} \n valores negativos {negativos}")
#força guido
