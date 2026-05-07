media: list = (lambda nums: ([i for i in nums]))(
    [int(input(f"Insira a altura da {i + 1} pessoa: ")) for i in range(20)]
)
print(f"Media das alturas {sum(media) / len(media)}")
