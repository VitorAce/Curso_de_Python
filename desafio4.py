''' 
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ela 
'''
n = input('Digitel algo:')
print(type(n))
print('O valor é numerico ?{}'.format(n.isnumeric()))
print('O valor é alfabetico e numnerico ?' ,n.isalnum())
print('O valor é numerico ?' ,n.isalpha())
print('O valor é decimal ?' ,n.isdecimal())
