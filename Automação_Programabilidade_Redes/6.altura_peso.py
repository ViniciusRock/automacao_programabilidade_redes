#Tendo como entrada a altura e o sexo de uma pessoa,
#Construa um algoritmo que calcule e imprima seu peso ideal,
#utilizando as seguintes fórmulas:
#- Para homens: (72.7 * h) – 58
#- Para mulheres: (62.1*h) - 44.7
print('Cálculo de peso ideal')
print('Se identifique')
print('Para homem: H,h, ou homem','Para Mulher: M,m ou mulher')
sexo = input("Sexo:")
if sexo.upper() == 'H' or 'HOMEM':
    print(sexo.upper())
    altura = float(input("Informe sua altura:"))
    pesoh = (72.7 * altura) - 58
    print('Seu peso ideal é:',pesoh)
else:
    print(sexo.upper())
    altura = float(input("Informe sua altura:"))
    pesom = (62.1 * altura) - 44.7
    print('Seu peso ideal é:',pesom)