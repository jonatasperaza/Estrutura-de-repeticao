par, impar = (lambda nums: ([n for n in nums if n % 2 == 0], [n for n in nums if n % 2 != 0]))([int(input("Insira um número: ")) for _ in range(10)])


print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
