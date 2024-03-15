#Escreva um algoritmo para ler 2 valores e escrever o maior deles.
v1 = int(input('Valor 1:'))
v2 = int(input('Valor 2:'))

if v1 > v2:
    print(v1,'é maior')
elif v2 > v1:
    print(v2,'é maior')
else:
    print('Valores idênticos')