import random

print(random.randint(1, 100))
print(random.randint(1, 100))
print()

alunos = ['José', 'João', 'Pedro', 'Lucas', 'Tiago']
print(random.choice(alunos))
print(random.choice(alunos))
random.shuffle(alunos)
print(alunos)
random.shuffle(alunos)
print(alunos)