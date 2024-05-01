''' Dissecando Variáveis
Faça um programa que leia algo pelo teclado de mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
Métodos dos objetos strings
'''
user_enter = input("Digite algo:\n")

print(f'O tipo primitivo da sua entrada é: {type(user_enter)}')
print(f'Só tem espaços: {user_enter.isspace()}')
print(f'É um número? {user_enter.isnumeric()}')
print(f'É alfabético? {user_enter.isalpha()}')
print(f'É alfanumérico? {user_enter.isalnum()}')
print(f'É minúsculas? {user_enter.islower()}')
print(f'É Maiúscula? {user_enter.isupper()}')
print(f'Está Capitalizada? {user_enter.istitle()}')






