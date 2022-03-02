# 8) Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Resolução do Exercício 8:
distancia = float(input('Uma distância em metros: '))

print(f'A medida de {distancia} corresponde a ')
print(f'{distancia/1000}km')
print(f'{distancia/100}hm')
print(f'{distancia/10}dam')
print(f'{distancia*10:.0f}dm')
print(f'{distancia*100:.0f}cm')
print(f'{distancia*1000:.0f}m')
