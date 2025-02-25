#include <stdio.h>
#include <stdlib.h>

void caminhadabraba(int arvore[], int x, int node, int* caminho, int* indice) {
    if (node >= x) // Verifica se o nó está fora do limite
        return;

    if (arvore[node] != -1) { // Verifica se o nó não é nulo
        caminho[(*indice)++] = arvore[node]; // Visita o nó
        caminhadabraba(arvore, x, 2 * node + 1, caminho, indice); // Vai para o filho esquerdo
        if (2 * node + 1 < x && arvore[2 * node + 1] != -1) // Se o filho esquerdo não for nulo
            caminho[(*indice)++] = arvore[node]; // Volta para o nó atual
        caminhadabraba(arvore, x, 2 * node + 2, caminho, indice); // Vai para o filho direito
        if (2 * node + 2 < x && arvore[2 * node + 2] != -1) // Se o filho direito não for nulo
            caminho[(*indice)++] = arvore[node]; // Volta para o nó atual
    }
}

int main() {
    int x;
    printf("Digite o número de nós na árvore: ");
    scanf("%d", &x);

    while (x!= 0) { // Loop para lidar com múltiplos casos de teste
        int* arvore = (int*)malloc(x * sizeof(int)); // Aloca memória para a árvore

        printf("Digite os elementos da árvore (-1 para nós vazios): ");
        for (int i = 0; i < x; i++) {
            scanf("%d", &arvore[i]);
        }

        int* caminho = (int*)malloc(x * 3 * sizeof(int)); // Aloca memória para o passeio de caminho
        int indice = 0; // Inicializa o índice

        caminhadabraba(arvore, x, 0, caminho, &indice);

        printf("Passeio de caminho: ");
        for (int i = 0; i < indice; i++) {
            printf("%d ", caminho[i]);
        }
        printf("\n");

        free(arvore); // Libera a memória alocada para a árvore
        free(caminho); // Libera a memória alocada para o passeio de caminho

        // Lê o número de nós na próxima árvore
        printf("\nDigite o número de nós na próxima árvore (ou 0 para encerrar): ");
        scanf("%d", &x);
    }

    return 0;
}
