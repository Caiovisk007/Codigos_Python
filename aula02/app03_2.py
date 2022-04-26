"""
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

vetor.reverse()
print("Vetor invertido: ", vetor)
"""

vetor = []
i = 1
while i <= 10:
    n = float(input("Digite um número: "))
    vetor.append(n)
    i += 1
print("")
i = 9
while i >= 0:
    print(vetor[i])
    i -= 1