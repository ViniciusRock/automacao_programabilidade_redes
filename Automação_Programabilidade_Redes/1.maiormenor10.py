#Escreva um algoritmo para ler um valor e escrever a mensagem
#‘É maior que 10 ‘ se o valor lido for maior que 10, caso contrário 
#escrever ‘NÃO é maior que 10’.
valor = int(input("Digite um valor:"))
if valor > 10:
    print('É maior que 10')
elif valor < 10:
    print('NÃO é maior que 10')
#Exceção
else:
    print('Valor é igual a 10')
