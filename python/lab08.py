###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
# Nome: Arthur Dionizio
# RA: 250814

n = int(input())
nn = n
pontuacao = ['.', ',', ':', ';', '!', '?']

def palindrome(s):
    for i in range(0, len(s)):
        if s[i] != s[- i - 1]:
            return False
    return True

freq = {}

while n > 0:
    l = input().split(" ")

    for i in range(0, len(l)):
        l[i] = l[i].lower()
        for ponto in pontuacao:
            l[i] = l[i].replace(ponto, '')

        if palindrome(l[i]):
            if l[i] in freq.keys():
                freq[l[i]] += 1
            else:
                freq[l[i]] = 1

    n -= 1

for x in freq.keys():
    print (x, freq[x])