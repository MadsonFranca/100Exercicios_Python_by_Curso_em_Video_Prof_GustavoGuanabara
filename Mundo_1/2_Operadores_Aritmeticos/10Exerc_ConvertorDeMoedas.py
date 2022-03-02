# 10) Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Resolução do Exercício 10:
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 5.16

print(f'Com R${dinheiro:.2f} você pode comprar US${dinheiro*dolar:.2f}!')