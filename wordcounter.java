import java.util.concurrent.locks.ReentrantLock;

class WordCounter implements Runnable {
    private static int totalWordCount = 0;
    private static ReentrantLock lock = new ReentrantLock();
    private String[] data;

    public WordCounter(String[] data) {
        this.data = data;
    }

    @Override
    public void run() {
        int localCount = data.length; // Contando palavras na parte do array
        lock.lock();
        try {
            totalWordCount += localCount;
        } finally {
            lock.unlock();
        }
    }

    public static int getTotalWordCount() {
        return totalWordCount;
    }

    public static void main(String[] args) throws InterruptedException {
        String[] data = {"word1", "word2", "word3", "word4"}; // Simulando dados
        int numThreads = 4;
        Thread[] threads = new Thread[numThreads];

        for (int i = 0; i < numThreads; i++) {
            threads[i] = new Thread(new WordCounter(data));
            threads[i].start();
        }
        
        for (Thread t : threads) {
            t.join();
        }

        System.out.println("Total Word Count: " + getTotalWordCount());
    }
}
