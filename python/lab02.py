#!/usr/bin/env python
# coding: utf-8

# In[52]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Trem das Onze
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################
###
import math
# Leitura de dados
X1 = int(input())
Y1 = int(input())
W1 = float(input())
Z1 = float(input())
X2 = int(input())
Y2 = int(input())
W2 = int(input())
Z2 = int(input())
# Cálculo do tempo gasto para chegar a parada do trem
"O tempo gasto é calculado pela divisão entre desclocamento e velocidade."
"Para realizar essa divisão, devemos converter a velocidade para km/minutos"
t1 = W1 / (Z1/60)
t2 = W2 / (Z2/60)

"Arredondando o valor obtido para cima"
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
t1 = round_up(t1)
t2 = round_up(t2)
"Precisa dar tempo de pegar o primeiro ônibus e precisa dar tempo de chegar à estação às 11PM"
"Para descobrir ambos, preciso de uma maneira de calcular de converter o tempo gasto em horas e minutos"
tempo1 = t1 + Y1
tempo2 = t2 + Y2
c1 = X1
c2 = X2
cm1 = tempo1
cm2 = tempo2
if tempo1 >= 60: 
    c1 += (tempo1//60)
    cm1 = tempo1 - ((tempo1//60)*60)
if tempo2 >= 60:
    c2 += (tempo2//60)
    cm2 = tempo2 - ((tempo2//60)*60)

if c1 > X2:
    print(False)
if c1 == X2 and cm1>=Y2:
    print(False)
if (c1 == X2 and cm1 < Y2) or (c1 < X2):
    if (c2 >= 11):
        print(False)
    elif (c2 < 11):
        print(True)
###
# Impressão da resposta


# In[ ]:





# In[ ]:




