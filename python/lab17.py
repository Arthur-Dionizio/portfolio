#!/usr/bin/env python
# coding: utf-8

# In[26]:


###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Tradutor de Código Morse
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################
dicionario = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '[AEFHIJLPRSUVW]':'.*', '[BCDGKMNOQTXYZ]':'-*', 
                    '[FHISUV]':'..*', '[AJLPRW]':'.-*', '[GMOQZ]':'--*',
                    '[BCDKNXY]':'-.*', '[HSV]':'...*', '[FU]':'..-*',
                    '[LR]':'.-.*', '[JPW]':'.--*', '[GQZ]':'--.*',
                    '[O]':'---*', '[BDX]':'-..*', '[CKY]':'-.-*',
                    '[V]':'...-*', '[B]':'-...*', '[C]':'-.-.*', '[F]':'..-.*',
                    '[H]':'....*', '[J]':'.---*', '[L]':'.-..*', '[P]':'.--.*',
                    '[Q]':'--.-*', '[V]':'...-*', '[X]':'-..-*', '[Y]':'-.--*', '[Z]':'--..*'}
def traduzir(texto):
    texto += ' '
    tradutor = ''
    aaa = ''
    for letra in texto:
        if (letra != ' '):
            i = 0
            aaa += letra
        else:
            i += 1
            if i == 2 :
                tradutor += ' '
            else:
                tradutor += list(dicionario.keys())[list(dicionario
                .values()).index(aaa)]
                aaa = ''
    return tradutor
 
def funcao():
    texto = str(input())
    produto = traduzir(texto)
    print(produto)
 
resposta = funcao()


# In[ ]:




