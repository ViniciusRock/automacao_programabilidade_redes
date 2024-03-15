#Escreva um algoritmo para ler o ano de nascimento de uma pessoa 
#e escrever uma mensagem que diga se ela poderá ou não votar este ano
#(não é necessário considerar o mês em que ela nasceu).
ano = int(input('Informe o ano de nascimento:'))

#variável guardando o ano atual
ano_atual = 2024

#variavel idade > Calcula o ano atual subtraindo o ano informado
#idade = 2024 - ano
idade = ano_atual - ano

##Se idade for maior ou igual que 16, já pode votar, senão não pode.
if idade >=16:
    print('Poderá votar este ano')
else:
    print('Não poderá votar este ano')

