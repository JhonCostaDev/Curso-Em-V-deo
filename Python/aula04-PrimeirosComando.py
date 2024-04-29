#print('olá mundo!!!')# todos comando são funções e vão dentro de parenteses!
#print('a soma é: ','7'+'4')
#NO PYTHON TODA VARIÁVEL É UM OBJETO
nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
peso = input('Qual é o seu peso?  ' )
peso = float(peso)
altura = input("Qual é sua altura? ")
altura = float(altura)
imc = peso//(altura*altura) # divisão // ignora a parte decimal do resultado!

if imc < 30 :
    print('-----------------------------------------')
    print('Olá ', nome, 'você tem ', idade, 'anos')
    print('e o seu IMC é de: ', imc)
    print('Abaixo do Peso')
else:
    print('-----------------------------------------')
    print('Olá ', nome, 'você tem ', idade, 'anos')
    print('e o seu IMC é de: ', imc)
    print('Acima do Peso')




