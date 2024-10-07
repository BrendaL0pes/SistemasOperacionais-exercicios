#include <stdio.h>
#include <pthread.h>

void* process_data(void* arg) {
    int* data = (int*)arg;
    for (int i = 0; i < 4; i++) {
        data[i] *= 2;  // Exemplo de processamento
    }
    return NULL;
}

int main() {
    int data[] = {1, 2, 3, 4};
    int num_threads = 4;
    pthread_t threads[num_threads];

    for (int i = 0; i < num_threads; i++) {
        pthread_create(&threads[i], NULL, process_data, data);
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Processed data: ");
    for (int i = 0; i < 4; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");
    return 0;
}
