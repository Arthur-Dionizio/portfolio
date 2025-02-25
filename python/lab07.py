###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Luiz Felipe de Oliveira Barbosa Nunes
# RA: 255403
###################################################

# leitura de dados

d = int(input())
h = int(input())
m = int(input())
e = input()
p = input()
d = d - 1

# valor do ingresso inteiro
# Utilizei uma tabela 'preco_tabela[x][y]', onde x = [0, 1], e y = [0, 1, 2, 3, 4, 5, 6].
preco_tabela = [
    [30, 15, 15, 15, 20, 20, 30],
    [30, 20, 20, 30, 30, 40, 40]
]

desconto_tabela = [
    [0.3, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2],
    [0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.2]
]

# Para x, 0 representa o periodo manhã/tarde, e 1, o periodo da noite
# valor a pagar
if (h == 18 and m >= 30) or (h >= 19):
    periodo = 1 
else: periodo = 0


preco = preco_tabela[periodo][d]

desconto = 0
if(e == 'S'):
    desconto = 0.5
elif(p == 'C'):
     desconto = desconto_tabela[periodo][d]

ingresso = preco * (1 - desconto)

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))

