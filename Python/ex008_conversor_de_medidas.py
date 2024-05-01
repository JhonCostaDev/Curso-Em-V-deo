'''
008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

'''

print("Conversor de Medidas")

user_input = float(input("Digite uma distância em metros:\n"))

print(f'A distância de {user_input}metros correspônde a:\n{int(user_input*100)} centímetros e {int(user_input*1000)} milímetros.')
