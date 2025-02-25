#!/usr/bin/env python
# coding: utf-8

# In[3]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################

# Leitura de dados
estoque = {}
while True:
    N = input()
    if N == "FIM":
        break
    a = N.split(" : ")
    Produto = a[0]
    X = int(a[1])

    if Produto not in estoque:
        estoque[Produto] = {}
        estoque[Produto]["Produto"] = Produto
        estoque[Produto]["Quantidade em Estoque"] = 0
        estoque[Produto]["Pedidos de Compra"] = 0
        estoque[Produto]["Pedidos de Venda"] = 0

    if estoque[Produto]["Quantidade em Estoque"] + X < 0:
        print("Quantidade indisponivel para a venda de ",-X," unidade(s) do produto ",Produto,".")
    else:
        estoque[Produto]["Quantidade em Estoque"] += X

    if X > 0:
        estoque[Produto]["Pedidos de Compra"] += 1
     
    elif X < 0 and estoque[Produto]["Quantidade em Estoque"] + X > 0:
        estoque[Produto]["Pedidos de Venda"] += 1
    

estoquefinal = sorted(estoque.keys())
for entry in estoquefinal:
    if estoque[entry]["Pedidos de Compra"] > 0:
      print("Produto:",estoque[entry]["Produto"])
      print("Quantidade em Estoque:",estoque[entry]["Quantidade em Estoque"])
      print("Pedidos de Compra:",estoque[entry]["Pedidos de Compra"])
      print("Pedidos de Venda:",estoque[entry]["Pedidos de Venda"])
        


# In[ ]:





# In[ ]:




