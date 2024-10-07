class ImageProcessor implements Runnable {
    private int[] data;

    public ImageProcessor(int[] data) {
        this.data = data;
    }

    @Override
    public void run() {
        for (int i = 0; i < data.length; i++) {
            data[i] = process(data[i]);  // Processando dados
        }
    }

    private int process(int pixel) {
        return pixel * 2;  // Exemplo de operação de filtro
    }

    public static void main(String[] args) throws InterruptedException {
        int[] data = {1, 2, 3, 4};  // Simulando uma imagem
        int numThreads = 4;
        Thread[] threads = new Thread[numThreads];

        for (int i = 0; i < numThreads; i++) {
            threads[i] = new Thread(new ImageProcessor(data));
            threads[i].start();
        }

        for (Thread t : threads) {
            t.join();
        }

        System.out.println("Processed data:");
        for (int i : data) {
            System.out.print(i + " ");
        }
    }
}
