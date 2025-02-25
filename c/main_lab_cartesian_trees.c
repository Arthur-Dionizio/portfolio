#include <stdio.h>
#include <stdlib.h>

struct CartesianTree {
    int *values;
    int *parentOf;
    int size;
    int capacity;
};

void initCartesianTree(struct CartesianTree *tree, int capacity) {
    tree->size = 0;
    tree->capacity = capacity;
    tree->values = (int *)malloc(capacity * sizeof(int));
    tree->parentOf = (int *)malloc(capacity * sizeof(int));
    for (int i = 0; i < capacity; i++) {
        tree->parentOf[i] = -1;
    }
}

void freeCartesianTree(struct CartesianTree *tree) {
    free(tree->values);
    free(tree->parentOf);
}

void push(struct CartesianTree *tree, int value) {
    int added = tree->size; // index of the new value
    int parent = added - 1; // index of the most recently added value
    int child = -1; // a NIL pointer
    tree->values[added] = value;
    tree->size++;

    while (parent >= 0 && tree->values[parent] > value) {
        child = parent;
        parent = tree->parentOf[parent]; // move up
    }

    // inject the new node between child and parent
    tree->parentOf[added] = parent;
    if (child >= 0) tree->parentOf[child] = added;
}

void extend(struct CartesianTree *tree, int *values, int length) {
    for (int i = 0; i < length; i++)
        push(tree, values[i]);
}

void printIndexesByLevel(struct CartesianTree *tree) {
    int *level = (int *)malloc(tree->capacity * sizeof(int));
    int *nextLevel = (int *)malloc(tree->capacity * sizeof(int));
    int currentLevelCount = 0, nextLevelCount = 0;

    // Find the root (which has parentOf value -1)
    for (int i = 0; i < tree->size; i++) {
        if (tree->parentOf[i] == -1) {
            level[currentLevelCount++] = i;
            break;
        }
    }

    while (currentLevelCount > 0) {
        nextLevelCount = 0;
        for (int i = 0; i < currentLevelCount; i++) {
            int currentNode = level[i];
            printf("%d ", currentNode);
            for (int j = 0; j < tree->size; j++) {
                if (tree->parentOf[j] == currentNode) {
                    nextLevel[nextLevelCount++] = j;
                }
            }
        }
        printf("\n");
        currentLevelCount = nextLevelCount;
        for (int i = 0; i < nextLevelCount; i++) {
            level[i] = nextLevel[i];
        }
    }

    free(level);
    free(nextLevel);
}

int main() {
    struct CartesianTree tree;
    int n;

    while (1) {
        scanf("%d", &n);
        if (n == 0) break;

        initCartesianTree(&tree, n);

        int *values = (int *)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++)
            scanf("%d", &values[i]);

        extend(&tree, values, n);

        printIndexesByLevel(&tree);
        printf("\n");

        free(values);
        freeCartesianTree(&tree);
    }

    return 0;
}
