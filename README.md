# Curso-Em-V-deo
Meus Estudos na Plataforma Curso em Vídeo

EN OF PYTHON
Bonito é melhor que feio.
Explícito é melhor que implícito
Simples é melhor que Complexo
Complexo é melhor que complicado.
Linear é melhor que aninhado.
Esparso é melhor que denso.
Casos especiais não são especiais o bastante para quebrar as regras.
Ainda que praticidade vença a pureza;
Erros numca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deveria haver um - e preferencialmente só um - modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês
Agora é melhor que nunca
Embora nunca frequentemente seja melhor que já
Se a implementação é dificil de explicar, é uma má idéia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande idéia - vamos ter mais dessas.


# FASE 06 - TIPOS PRIMITIVOS
int: números inteiros;
float: números reais, ponto flutuante;
bool: True / False - Primeira letra sempre maiúscula.
str: strings sempre terão que estar entre aspas.

# Aula07-OPERADORES ARITMÉTICOS (BINÁRIOS)

ADIÇÃO (+):
5+2 == 7

SUBTRAÇÃO (-):
5-2== 3

MULTIPLICAÇÃO(*):
5*2== 10

DIVISÃO(/):
5/2== 2.5

POTÊNCIA (**):
5**2== 25
pow(5,2) == 25 - outra forma de fazer potencias.

DIVISÃO INTEIRA (//):
5//2== 2

DIVISÃO QUOCIENTE(%) :
5%2== 1

ORDEM DE PRECEDÊNCIA OPERADORES
1: (PARÊNTESES)
2: ** POTENCIAS
3: *MULTIPLICAÇÃO /DIVISÃO //DIVISÃO INTEIRA %DIVISÃO QUOCIENTE.
4: + ADIÇÃO - SUBTRAÇÃO

CALCULAR A RAIZ QUADRADA DE UM NÚMERO, É A MESMA COISA QUE CALCULAR A POTENCIA DELE POR 1/2
RAIZ QUADRADA DE 144**(1/2) == 12
CALCULAR A RAIZ CUBICA DE UM NÚMERO, É A MESMA COISA QUE CALCULAR A POTENCIA DELE POR 1/3
127**(1/2)== 5.026525695313479

MACETES
'OI'* 5
Out[3]: 'OIOIOIOIOI'
'='*20
Out[4]: '===================='
print('='*40)
========================================
print(127**(1/3))
nome = input("qual é o seu nome? ")
print("Prazer em te conhecer {:>20}!".format(nome))
print("Prazer em te conhecer {:<20}!".format(nome))
print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te concern {:=^20}!".format(nome))
