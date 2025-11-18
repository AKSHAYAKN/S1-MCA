#include <stdio.h>
#define MAX 30
int parent[MAX];
int find(int x) {
    while (parent[x] != x)
        x = parent[x];
    return x;
}


void union_set(int a, int b) {
    int p1 = find(a);
    int p2 = find(b);
    parent[p1] = p2;
}

int main() {
    int V, E;
    int u[100], v[100], w[100];

    printf("Enter number of vertices: ");
    scanf("%d", &V);
    printf("Enter number of edges: ");
    scanf("%d", &E);

    printf("Enter edges (u v weight):\n");
    for (int i = 0; i < E; i++) {
        scanf("%d %d %d", &u[i], &v[i], &w[i]);
    }

  
    for (int i = 0; i < V; i++)
        parent[i] = i;

    
    for (int i = 0; i < E - 1; i++) {
        for (int j = 0; j < E - i - 1; j++) {
            if (w[j] > w[j + 1]) {
                int temp;

                temp = w[j]; w[j] = w[j + 1]; w[j + 1] = temp;
                temp = u[j]; u[j] = u[j + 1]; u[j + 1] = temp;
                temp = v[j]; v[j] = v[j + 1]; v[j + 1] = temp;
            }
        }
    }

    int total = 0;
    printf("\nEdges in MST:\n");

    for (int i = 0; i < E; i++) {
        int a = find(u[i]);
        int b = find(v[i]);

        if (a != b) {
            printf("%d -- %d  weight = %d\n", u[i], v[i], w[i]);
            total += w[i];
            union_set(a, b);
        }
    }

    printf("\nTotal weight of MST = %d\n", total);

    return 0;
}

