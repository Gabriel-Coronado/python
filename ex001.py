nome = input('Digite seu nome: ')
print('Bem vindo {}!'.format(nome))

nasc = int(input('Que ano vc nasceu?'))
atual =int(input('Digite o ano atual:')) 
idade = atual - nasc

print('Sua idade é {}'.format(idade))