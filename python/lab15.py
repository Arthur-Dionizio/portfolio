def selecao_e_insercao(lista):
    trocas = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            trocas += 1
        lista[j + 1] = chave
        print(lista.copy())
    return trocas


def bubble_up_and_down(lista):
    trocas = 0
    n = len(lista)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocas += 1
                sorted = False
        if not sorted:
            print(lista.copy())
        if sorted:
            break
        sorted = True
        for i in range(n - 2, -1, -1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocas += 1
                sorted = False
        if not sorted:
            print(lista.copy())
    return trocas


lista = [int(a) for a in input().split()]

print("Algoritmo Seleção e Inserção:")
copia_lista = lista.copy()
X = selecao_e_insercao(copia_lista)
print("Trocas realizadas:", X)
print()
print("Algoritmo Bubble Up and Down:")
copia_lista = lista.copy()
Y = bubble_up_and_down(copia_lista)
print("Trocas realizadas:", Y)

'''
te enviarei o código inteiro e quero que mude a primeira função de modo que ela se adeque ao formato de saída especificado no fim do código
Leve em consideração a segunda função e o modo que sua saída é impressa, quero que imprima a saída da primeira função do mesmo jeito

No fim, o que eu busco é uma saída no formato dos exemplos abaixo:
Entrada 1:
5 7 2 8 1 4 3 6

Saída 1:
Algoritmo Seleção e Inserção:
[1, 5, 7, 2, 8, 4, 3, 6]
[1, 2, 5, 7, 8, 4, 3, 6]
[1, 2, 3, 5, 7, 8, 4, 6]
[1, 2, 3, 4, 5, 7, 8, 6]
[1, 2, 3, 4, 5, 6, 7, 8]
Trocas realizadas: 15

Algoritmo Bubble Up and Down:
[5, 2, 7, 1, 4, 3, 6, 8]
[1, 5, 2, 7, 3, 4, 6, 8]
[1, 2, 5, 3, 4, 6, 7, 8]
[1, 2, 3, 5, 4, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
Trocas realizadas: 15

Entrada 2:
2 8 5 4 1 6

Saída 2:
Algoritmo Seleção e Inserção:
[1, 2, 8, 5, 4, 6]
[1, 2, 4, 8, 5, 6]
[1, 2, 4, 5, 8, 6]
[1, 2, 4, 5, 6, 8]
Trocas realizadas: 8

Algoritmo Bubble Up and Down:
[2, 5, 4, 1, 6, 8]
[1, 2, 5, 4, 6, 8]
[1, 2, 4, 5, 6, 8]
Trocas realizadas: 8

Entrada 3:
9 8 7 6 5 4 3 2 1

Saída 3:
Algoritmo Seleção e Inserção:
[1, 9, 8, 7, 6, 5, 4, 3, 2]
[1, 2, 9, 8, 7, 6, 5, 4, 3]
[1, 2, 3, 9, 8, 7, 6, 5, 4]
[1, 2, 3, 4, 9, 8, 7, 6, 5]
[1, 2, 3, 4, 5, 9, 8, 7, 6]
[1, 2, 3, 4, 5, 6, 9, 8, 7]
[1, 2, 3, 4, 5, 6, 7, 9, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Trocas realizadas: 36

Algoritmo Bubble Up and Down:
[8, 7, 6, 5, 4, 3, 2, 1, 9]
[1, 8, 7, 6, 5, 4, 3, 2, 9]
[1, 7, 6, 5, 4, 3, 2, 8, 9]
[1, 2, 7, 6, 5, 4, 3, 8, 9]
[1, 2, 6, 5, 4, 3, 7, 8, 9]
[1, 2, 3, 6, 5, 4, 7, 8, 9]
[1, 2, 3, 5, 4, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Trocas realizadas: 36