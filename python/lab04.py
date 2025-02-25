#!/usr/bin/env python
# coding: utf-8

# In[50]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Picos e Vales I
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################

# leitura e verificação dos picos e vales
altura = int(input())
picos = 0
vales = 0
lista = []
i = 0
while altura != 0:
    lista.append(altura)
    altura = int(input())
    
for i in range(1, len(lista)-1):
    if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
        picos += 1
        i = i+1
    elif lista[i]<lista[i-1] and lista[i]<lista[i+1]:
        vales += 1
        i += 1
    else:
        i += 1
print("Quantidade de picos:", picos)
print("Quantidade de vales:", vales)


# ### 

# ##### 
