#!/usr/bin/env python
# coding: utf-8

# In[9]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Escolha da Missão
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################
"""
1-nivel qqr, pelo menos 30 PA e 10 PD, recebe 25 moedas; lucro de 25 moedas
2-nivel qqr, pelo menos 30 PD e 30 moedas, recebe 40 moedas; lucro de 10 moedas
3- pelo menos nvl 3, PA menor que PD e 50 moedas, recebe 100 moedas; lucro de 50 moedas
4- pelo menos nvl 3, 20 moedas de ouro OU (20 PA e 30 PD), recebe 40 moedas; lucro de 20 ou 40 moedas
5- pelo menos nvl 5, 40 PA e 50 PD, 50 moedas, recebe 130 moedas; lucro de 80 moedas
6- pelo menos nvl 5 e 50 PD, recebendo 3o moedas; se tiver tbm 50 PA, recebe 60 moedas no total; lucro de 30 ou 60 moedas
rank das missoes por lucro: 5 - 6(se tiver 50 PA) - 3 - 4(se tiver 20 PA e 30 PD) - 6(easy) - 1 - 4(easy) - 2
"""
# leitura de dados
nivel = int(input())
PA = int(input())
PD = int(input())
moedas = int(input())
# Escolha da missão
if nivel >= 5 and PA >= 40 and PD >= 50 and moedas >= 50:
    print('missão escolhida:', 5)
    print('moedas de ouro:', moedas + 80)
elif nivel >= 5 and PA >= 50 and PD >= 50:
    print('missão escolhida:', 6)
    print('moedas de ouro:', moedas + 60)
elif nivel >= 3 and PA<PD and moedas >= 50:
    print('missão escolhida:', 3)
    print('moedas de ouro:', moedas + 50)
elif nivel >= 3 and PA >= 20 and PD >= 30:
    print('missão escolhida:', 4)
    print('moedas de ouro:', moedas + 40)
elif nivel >= 5 and PD >= 50:
    print('missão escolhida:', 6)
    print('moedas de ouro:', moedas + 30)
elif PA >= 30 and PD >= 10:
    print('missão escolhida:', 1)
    print('moedas de ouro:', moedas + 25)
elif nivel >= 3 and moedas >= 20:
    print('missão escolhida:', 4)
    print('moedas de ouro:', moedas + 20)
elif PD >= 30 and moedas >= 30:
    print('missão escolhida:', 2)
    print('moedas de ouro:', moedas + 10)
else:
    print('missão escolhida:', 0)
    print('moedas de ouro:', moedas)


# In[ ]:





# In[ ]:




