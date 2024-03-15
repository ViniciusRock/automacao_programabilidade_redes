#Escreva um algoritmo que verifique a validade de uma senha fornecida
#pelo usuário.
#A senha válida é a palavra UNISENAC. Deve ser impresso as
#seguintes mensagens:
#- Acesso Permitido, caso a senha seja válida.
#- Acesso Negado, caso a senha seja inválida.
senha = input('Insira a senha para login:')
if senha == 'UNISENAC':
    print('Acesso Permitido!')
else:
    print('Acesso Negado!')