par, impar = (lambda nums: ([i for i in nums if i % 2 == 0], [i for i in nums if i % 2 != 0]))([i for i in range(101)])

print(sum(par))
print(sum(impar))
