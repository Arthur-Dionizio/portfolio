##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos
M = int(input())
while M != 0:
    reversa = torre.copy()
    if M == 1:
        pass
    else:
        del reversa[M:]
        reversa.reverse()
        for j in range(0, M):
            torre[j] = reversa[j]
    M = int(input())

# Impressão da saída
if torre == sorted(torre):
    print("Torre estavel")
else:
    print("Torre instavel")