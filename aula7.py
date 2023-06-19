'''
Aula 7 - Operadores aritméticos 
+ Adição             ** Potência 
- Subtração          // Divisão Inteira
* Multiplicação      %  Resto da Dvisão
/ Divisão
= Significa atribuição
== Funciona como o termo de igualdade da matématica
5 + 2 == 7           5 ** 2 == 25
5 - 2 == 3           5 // 2 == 2 (Resultado)
5 * 2 == 10          5 %  2 == 1 (Resto)
5 / 2 == 2,5
Faça uma divisão de 5 por 2, nela hávera resultado 2 com resto 1
Ordem de Precedência
1 ()
2 **
3 * / // %
4 + -
(Você executar um programa e ele funcionar, nem sempre significa que ele
está certo)
Exemplo:
5 + 3 * 2
5 + 6 == 11

3 * 5 + 4 ** 2 
15 + 16 == 31

3 * ( 5 + 4 ) ** 2
3 * 9 ** 2
3 * 81 == 243

Prática
5+3*2 == 11
5**2 == 25

19//2 == 9 (Dvisão inteira)
19/2 == 9.5 (Divisão)

10%2 == 0 (Resto da divisão)
122%3 == 2

pow(4,3) == 64 (Raiz cúbica)

81**(1/2) == 9 (Raiz quadrada)
25**(1/2) == 5 

127**(1/3) == 5.026... (Raiz cúbica)

'Oi'+'Olá' (Não está servindo como soma e sim concatenação)
OiOlá

'Oi'*5
OiOiOiOiOi

'='*20
====================

print('='*20)
====================

nome = input('Qual é o seu nome?')
print('Prazer em te cohnecer{}!'. format(nome))
Qual é o seu nome? Vitor
Prazer em te cohnecer Vitor!

nome = input('Qual é o seu nome?')
print('Prazer em te cohnecer{:20}!'. format(nome)) (Adicionou 20 caracteres ao nome)
Qual é o seu nome? Vitor
Prazer em te cohnecer Vitor              !

nome = input('Qual é o seu nome?')
print('Prazer em te cohnecer{:>20}!'. format(nome)) (Adicionou 20 caracteres ao nome, com alinhamento a direita)
Qual é o seu nome?Vitor
Prazer em te cohnecer               Vitor!

nome = input('Qual é o seu nome?')
print('Prazer em te cohnecer{:<20}!'. format(nome)) (Adicionou 20 caracteres ao nome, com alinhamento a esquerda)
Qual é o seu nome? Vitor
Prazer em te cohnecer Vitor              !

nome = input('Qual é o seu nome?')
print('Prazer em te cohnecer{:^20}!'. format(nome)) (Adicionou 20 caracteres ao nome, com alinhamento central)
Qual é o seu nome?Vitor
Prazer em te cohnecer       Vitor        !

nome = input('Qual é o seu nome?')
print('Prazer em te cohnecer{:=^20}!'. format(nome))
Qual é o seu nome?Ana
Prazer em te cohnecer========Ana=========!

n1 = int(input('Um valor :'))
n2 = int(input('Digite outro valor :'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f}'. format(s,sub,m,d))
print('A divisão interia é {}, a potência é {}'.format(di,e))
Um valor :2
Digite outro valor :3
A soma é 5, a subtração é -1, a multiplicação é 6, a divisão é 0.667
A divisão interia é 0, a potência é 8

n1 = int(input('Um valor :'))
n2 = int(input('Digite outro valor :'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f}'. format(s,sub,m,d), end='')
print('A divisão interia é {}, a potência é {}'.format(di,e))
Um valor :4
Digite outro valor :5
A soma é 9, a subtração é -1, a multiplicação é 20, a divisão é 0.800A divisão interia é 0, a potência é 1024

n1 = int(input('Um valor :'))
n2 = int(input('Digite outro valor :'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n a subtração é {},\n a multiplicação é {},\n a divisão é {:.3f}'. format(s,sub,m,d), end='')
print('A divisão interia é {}, a potência é {}'.format(di,e))
Um valor :2
Digite outro valor :3
A soma é 5,
 a subtração é -1,
 a multiplicação é 6,
 a divisão é 0.667A divisão interia é 0, a potência é 8

Desafio 005
Faça um programa que leia um número inteiro e mostre na tela o seu suces
sor e seu antecessor
Desafio 006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz
quadrada
Desafio 007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mos
tre a sua média
Desafio 008 
Escreva um programa que leia um valor em mestros e o exiba convertido em
centímetros e milímetros
Desafio 009
Faça um programa que leia um número inteiro qualquer e mostre na tela sua
tabuada
Desafio 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostee quantos dólares ela pode comprar
Considere UU$ 1,00 = R$ 3,27
Desafio 011
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sa
bendo que cada litro de tinta pinta uma área de 2m2
Desafio 012
Faça um algoritmo que leia o preço de um prouto e mostre seu novo preço
com 5% de desconto
Desafio 013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento

'''
