#!/usr/bin/env python
# coding: utf-8

# In[53]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################

    #Eu preciso definir uma variável 'a' para que, quando ela for maior que 0, seja igual a X, e ,quando for menor que 0, seja
#igual a Y. X é a quantidade de unidades em estoque e Y é a quantidade de unidades vendidas.
    # The initial quantity is 0. Therefore, every Y that appears before an X is unvalid, once ''initial X'' = 0.
    # If X < Y, then X doesn´t change and ''Quantidade indisponível para a venda de Y unidades'' is printed.
    # If X > Y, then X = X - Y.
    
    # leitura de dados
a = int(input())
X = 0
Y = 0
Z = 0

while a != 0:
    if a > 0:
        X = X + a
    else:
        Y = a
        if (-Y) < X:
            X = X + Y
            Z = Z + 1
        else:
            print ("Quantidade indisponível para a venda de {} unidades.".format(-Y))
    a = int(input())

print ("Quantidade de vendas realizadas: {}".format(Z))
print ("Quantidade em estoque: {}".format(X))


# In[ ]:





# In[ ]:




