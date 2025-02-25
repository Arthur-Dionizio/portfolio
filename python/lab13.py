###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################
from collections import Counter
# Leitura de dados
listadevotos = []
voto = input()
listadevotos.append(voto)
variaveis = [];
variaveis.append(voto)
brancos = []
nulos = []
while voto != '0':
    voto = input()
    listadevotos.append(voto)
    if voto in variaveis:
        continue
    else:
        variaveis.append(voto)
    if voto == "Branco":
        brancos.append(voto)
    if voto == "Nulo":
        nulos.append(voto)
c = Counter(listadevotos)
variaveis.remove(variaveis[-1])
result = {}
for x in variaveis:
    if x == "Branco":
        continue
    if x == "Nulo":
        continue
    result[x] = c[x]

b = Counter(brancos)
n = Counter(nulos)
result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
for nome, vezes in result.items():
    print('{} {}'.format(nome,vezes))
print('Brancos {}'.format(len(brancos)))
print('Nulos {}'.format(len(nulos)))




"""def unique(list1):
 
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list

 
 
# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is", list1)
unique(list1)"""

# Saída de dados