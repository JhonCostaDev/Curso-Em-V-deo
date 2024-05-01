'''
006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

print('Dobro, Triplo e Raíz Quadrada')

user_number = int(input('Digite um número inteiro:\n'))

print(f'O dobro do número digitado é: {user_number * 2}\nO triplo do número digitado é: {user_number * 3}\nA raíz Quadrada do número digitado é: {int(user_number ** (1/2))} ')