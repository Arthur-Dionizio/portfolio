###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Cupons de Desconto II
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################
def calculate_discount(q1, x1, z1, q2, x2, z2, q3, x3, z3, purchases):
    n = len(purchases)
    max_discount = 0
    indices = (0, 0, 0)

    for i in range(n):
        for j in range(n):
            if j != i:
                for k in range(n):
                    if k != i and k != j:
                        used_indices = set()
                        used_indices.add(i)
                        used_indices.add(j)
                        used_indices.add(k)

                        q1_used = min(q1, len(used_indices))
                        q2_used = min(q2, len(used_indices) - q1_used)
                        q3_used = min(q3, len(used_indices) - q1_used - q2_used)

                        discount = 0

                        for idx, purchase in enumerate(purchases):
                            if idx == i and q1_used > 0 and purchase >= z1:
                                discount += x1
                                q1_used -= 1
                            elif idx == j and q2_used > 0:
                                discount2 = min(purchase * (x2 / 100), z2)
                                discount += discount2
                                q2_used -= 1
                            elif idx == k and q3_used > 0 and purchase >= z3:
                                discount += purchase * (x3 / 100)
                                q3_used -= 1

                        if discount > max_discount:
                            max_discount = discount
                            indices = (i + 1, j + 1, k + 1)

    return indices


# Entrada de dados
q1 = int(input())
x1 = int(input())
z1 = int(input())
q2 = int(input())
x2 = int(input())
z2 = int(input())
q3 = int(input())
x3 = int(input())
z3 = int(input())

n = int(input())
purchases = []
for _ in range(n):
    purchases.append(int(input()))

# Cálculo do desconto máximo
indices = calculate_discount(q1, x1, z1, q2, x2, z2, q3, x3, z3, purchases)

# Saída
print("Compra", indices[0], ": Cupom 1")
print("Compra", indices[1], ": Cupom 2")
print("Compra", indices[2], ": Cupom 3")
