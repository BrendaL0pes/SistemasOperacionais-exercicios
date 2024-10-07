import threading

total_word_count = 0
lock = threading.Lock()

def word_counter(data):
    global total_word_count
    local_count = len(data)  # Contagem de palavras
    with lock:
        total_word_count += local_count

if __name__ == "__main__":
    data = ["word1", "word2", "word3", "word4"]  # Simulando dados
    num_threads = 4
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=word_counter, args=(data,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Total Word Count: {total_word_count}")
