#include <stdio.h>
#include <pthread.h>

int total_word_count = 0;
pthread_mutex_t lock;

void* word_counter(void* arg) {
    char** data = (char**)arg;
    int local_count = 4; // Simulando contagem
    pthread_mutex_lock(&lock);
    total_word_count += local_count;
    pthread_mutex_unlock(&lock);
    return NULL;
}

int main() {
    char* data[] = {"word1", "word2", "word3", "word4"};
    int num_threads = 4;
    pthread_t threads[num_threads];

    pthread_mutex_init(&lock, NULL);

    for (int i = 0; i < num_threads; i++) {
        pthread_create(&threads[i], NULL, word_counter, data);
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&lock);
    printf("Total Word Count: %d\n", total_word_count);
    return 0;
}
