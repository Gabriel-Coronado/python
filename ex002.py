name = input('Digite seu nome em letras maiúsculas:')

if name.isupper() == True :
    print('Olá {}'.format(name))
else :
    print('Erro')