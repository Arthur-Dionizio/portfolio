###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################

# Entrada de dados
x1 = int(input())
z1 = int(input())
x2 = int(input())
z2 = int(input())
x3 = int(input())
z3 = int(input())

n = int(input())
aquisicoes = []
for _ in range(n):
    aquisicoes.append(int(input()))

# Criando a função
def calcular_disconto_maximo(x1, z1, x2, z2, x3, z3, aquisicoes):
    n = len(aquisicoes)
    maximodedescontopossivel = 0
    iii = (0, 0, 0)

    for i in range(n):
        for j in range(n):
            if j != i:
                for k in range(n):
                    if k != i and k != j:
                        discount = 0

                        if aquisicoes[i] >= z1:
                            discount += x1

                        discount2 = aquisicoes[j] * (x2 / 100)
                        if discount2 > z2:
                            discount2 = z2
                        discount += discount2

                        if aquisicoes[k] >= z3:
                            discount += aquisicoes[k] * (x3 / 100)

                        if discount > maximodedescontopossivel:
                            maximodedescontopossivel = discount
                            iii = (i + 1, j + 1, k + 1)

    return iii

iii = calcular_disconto_maximo(x1, z1, x2, z2, x3, z3, aquisicoes)

# Saída
print("Cupom 1:", iii[0])
print("Cupom 2:", iii[1])
print("Cupom 3:", iii[2])
"""
print('Cupom 1: {}'.format(i1))
print('Cupom 2: {}'.format(j1))
print('Cupom 3: {}'.format(k1))

for i in range(len(desconto1)):
    i1 = (desconto1.index(max(desconto1))) + 1
    for j in range(len(desconto2)), if j != i1:
        j1 = (desconto2.index(max(desconto2))) + 1
            for k in range(len(desconto3)), if (k != j1 and k != i1):
                k1 = (desconto3.index(max(desconto3))) + 1
if i1 == i2:
    lista_valores[i2-1] = 0
    descontoa11 = [i - j for i, j in zip(lista_valores, valores_cupom1)]
    if max(descontoa11) >= max(desconto1):
        i1 = (descontoa11.index(max(descontoa11))) + 1
        
    else:
        lista_valores[i1-1] = 0
        descontoa22 = [i - j for i, j in zip(lista_valores, valores_cupom2)]
        i2 = (descontoa22.index(max(descontoa22))) + 1
if i1 == i3:
    lista_valores[i1-1] = 0
    descontoa33 = [i - j for i, j in zip(lista_valores, valores_cupom3)]
    if max(descontoa33) >= max(desconto3):
        i3 = (descontoa33.index(max(descontoa33))) + 1    
    else:
        lista_valores[i3-1] = 0
        descontoa11 = [i - j for i, j in zip(lista_valores, valores_cupom1)]
        i1 = (descontoa11.index(max(descontoa11))) + 1
if i2 == i3:
    lista_valores[i2-1] = 0
    descontoa33 = [i - j for i, j in zip(lista_valores, valores_cupom3)]
    if max(descontoa33) >= max(desconto3):
        i3 = (descontoa33.index(max(descontoa33))) + 1    
    else:
        lista_valores[i3-1] = 0
        descontoa22 = [i - j for i, j in zip(lista_valores, valores_cupom2)]
        i2 = (descontoa22.index(max(descontoa22))) + 1
if i1 == i2:
    lista_valores[i2-1] = 0
    descontoaa11 = [i - j for i, j in zip(lista_valores, valores_cupom1)]
    if max(descontoaa11) >= max(descontoa1):
        i1 = (descontoa11.index(max(descontoa11))) + 1
    else:
        lista_valores[i1-1] = 0
        descontoaa22 = [i - j for i, j in zip(lista_valores, valores_cupom2)]
        i2 = (descontoaa22.index(max(descontoaa22))) + 1
if i1 == i3:
    lista_valores[i1-1] = 0
    descontoaa33 = [i - j for i, j in zip(lista_valores, valores_cupom3)]
    if max(descontoaa33) >= max(descontoa3):
        i3 = (descontoaa33.index(max(descontoaa33))) + 1    
    else:
        lista_valores[i3-1] = 0
        descontoaa11 = [i - j for i, j in zip(lista_valores, valores_cupom1)]
        i1 = (descontoaa11.index(max(descontoaa11))) + 1
if i2 == i3:
    lista_valores[i2-1] = 0
    descontoaa33 = [i - j for i, j in zip(lista_valores, valores_cupom3)]
    if max(descontoaa33) >= max(descontoa3):
        i3 = (descontoaa33.index(max(descontoaa33))) + 1    
    else:
        lista_valores[i3-1] = 0
        descontoaa22 = [i - j for i, j in zip(lista_valores, valores_cupom2)]
        i2 = (descontoaa22.index(max(descontoaa22))) + 1
# Impressão da resposta
print('Cupom 1: {}'.format(i1))
print('Cupom 2: {}'.format(i2))
print('Cupom 3: {}'.format(i3))

O cupom 1 dá X1 reais de desconto para compras acima de Z1 reais;
O cupom 2 dá X2% de desconto para qualquer compra, mas é limitado em Z2 reais, ou seja, 
caso os X2% de desconto seja maior que Z2 reais, o desconto final será de apenas Z2 reais;
O cupom 3 dá X3% de desconto para compras acima de Z3 reais.
    
Em caso de várias soluções com o mesmo resultado, use os seguintes critérios para desempate: 
    sempre dê preferência para a solução em que o cupom 1 foi usado na compra com menor índice. 
    Caso o empate persista, dê preferência para a solução em que o cupom 2 foi usado na compra 
    com menor índice. E, por fim, caso o empate ainda persista, 
    dê preferência para a solução em que o cupom 3 foi usado na compra com menor índice.
"""