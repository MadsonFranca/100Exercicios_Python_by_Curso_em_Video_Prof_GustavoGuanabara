# 4) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivieis sobre ele.

# Resolução do Exercício 4:
algo = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Só tem espaços? ', algo.isspace())
print(f'É um número? ', algo.isnumeric())
print(f'É alfabético? ', algo.isalpha())
print(f'Está em maiúsculo? ', algo.isupper())
print(f'Está em minúsculo? ', algo.islower())
print(f'Está capitalizado? ', algo.istitle())


