#!/usr/bin/env python
# coding: utf-8

# In[41]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Picos e Vales II
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################
terreno_1 = [int(i) for i in input().split()]
terreno_2 = [int(i) for i in input().split()]

picos1=0
vales1=0
lista1= []
picos2=0
vales2=0
lista2= []

for i in range(1, len(terreno_1)-1):
    if terreno_1[i]>terreno_1[i-1] and terreno_1[i]>terreno_1[i+1]:
        picos1 += 1
        i = i+1
        lista1.append("P")
    elif terreno_1[i]<terreno_1[i-1] and terreno_1[i]<terreno_1[i+1]:
        vales1 += 1
        i += 1
        lista1.append("V")
    else:
        i += 1

for i in range(1, len(terreno_2)-1):
    if terreno_2[i]>terreno_2[i-1] and terreno_2[i]>terreno_2[i+1]:
        picos2 += 1
        i = i+1
        lista2.append("P")
    elif terreno_2[i]<terreno_2[i-1] and terreno_2[i]<terreno_2[i+1]:
        vales2 += 1
        i += 1
        lista2.append("V")
    else:
        i += 1

string1 = ''
for i in lista1:
    string1 += '' + i
string2 = ''
for i in lista2:
    string2 += '' + i
    
if string1 == string2:
    print("As sequências e as quantidades de picos e vales são iguais")
elif string1.count('P') == string2.count('P') and string1.count('V') == string2.count('V'):
    print("As quantidades de picos e vales são iguais")
else:
    print("As sequências e as quantidades de picos e vales são diferentes")

