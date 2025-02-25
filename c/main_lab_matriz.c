#include <stdio.h>
#include <stdlib.h>

int main() {
    int k;
    scanf("%d", &k); // Entrada parte 1

    int max_i = 0, max_j = 0;
    int contagem = 0;
    int *vetor = malloc(3 * k * sizeof(int)); // Vetor para armazenar as coordenadas e valores da matriz

    // Lê as entradas da matriz e armazena diretamente no vetor
    for (int i = 0; i < k; i++) {
        int index = i * 3;
        scanf("%d %d %d", &vetor[index], &vetor[index + 1], &vetor[index + 2]);
        if (vetor[index] > max_i) max_i = vetor[index];
        if (vetor[index + 1] > max_j) max_j = vetor[index + 1];
        if (vetor[index + 2] != 0 && (i == 0 || vetor[index] != vetor[index - 3] || vetor[index + 1] != vetor[index - 2])) {
            // Incrementa contagem apenas se for uma nova entrada na matriz
            contagem++;
        }
    }

    // Inicializa a matriz com todos os elementos sendo 0
    int **matriz = (int **)calloc((max_i + 1), sizeof(int *));
    for (int i = 0; i <= max_i; i++) {
        matriz[i] = (int *)calloc((max_j + 1), sizeof(int));
    }

    // Preenche a matriz com os valores do vetor
    for (int i = 0; i < k; i++) {
        int index = i * 3;
        matriz[vetor[index]][vetor[index + 1]] = vetor[index + 2];
    }

    // Cria os vetores A_k e C_k
    int *A_k = malloc(contagem * sizeof(int));
    int *C_k = malloc(contagem * sizeof(int));
    int idx = 0;
    for (int i = 0; i < k; i++) {
        int index = i * 3;
        if (vetor[index + 2] != 0 && (i == 0 || vetor[index] != vetor[index - 3] || vetor[index + 1] != vetor[index - 2])) {
            A_k[idx] = vetor[index + 2];
            C_k[idx] = vetor[index + 1];
            idx++;
        }
    }

    // Cria o vetor R
    int *R = malloc((max_i + 2) * sizeof(int));
    int linha_atual = 0;
    idx = 0;
    for (int i = 0; i <= max_i; i++) {
        if (i == linha_atual) {
            R[i] = idx;
            while (linha_atual <= max_i && idx < contagem && vetor[idx * 3] == linha_atual) {
                idx++;
            }
            linha_atual++;
        } else {
            R[i] = R[linha_atual];
        }
    }
    R[max_i + 1] = contagem;

    // Consulta os elementos da matriz
    int consulta_i, consulta_j;
    while (1) {
        scanf("%d %d", &consulta_i, &consulta_j);
        if (consulta_i == -1 && consulta_j == -1) {
            break; // Condição de saída
        }

        // Verifica se os índices estão dentro dos limites da matriz
        if (consulta_i < 0 || consulta_i > max_i || consulta_j < 0 || consulta_j > max_j) {
            // Se estiverem fora dos limites, imprime que o valor do elemento é 0
            printf("(%d,%d) = 0\n", consulta_i, consulta_j);
            continue; // Pula para a próxima iteração do loop
        }

        // Recupera o elemento da matriz usando os vetores A_k, C_k e R
        int inicio = R[consulta_i];
        int final = R[consulta_i + 1];
        int encontrado = 0;
        for (int i = inicio; i < final; i++) {
            if (C_k[i] == consulta_j) {
                printf("(%d,%d) = %d\n", consulta_i, consulta_j, A_k[i]);
                encontrado = 1;
                break;
            }
        }
        if (!encontrado) {
            printf("(%d,%d) = 0\n", consulta_i, consulta_j);
        }
    }

    // Libera a memória alocada
    for (int i = 0; i <= max_i; i++) {
        free(matriz[i]);
    }
    free(matriz);
    free(vetor);
    free(A_k);
    free(C_k);
    free(R);

    return 0;
}
