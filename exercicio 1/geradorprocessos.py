import random
import time

# Definição dos estados dos processos
STATES = ["Novo", "Pronto", "Executando", "Esperando", "Encerrado"]

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.state = "Novo"  # Todos os processos começam como 'Novo'

    def transition(self):
        """Realiza a transição de estado aleatória."""
        if self.state == "Novo":
            self.state = "Pronto"
        elif self.state == "Pronto":
            self.state = random.choice(["Executando", "Esperando"])
        elif self.state == "Executando":
            self.state = random.choice(["Esperando", "Encerrado"])
        elif self.state == "Esperando":
            self.state = "Pronto"
        # 'Encerrado' é um estado final

    def is_terminated(self):
        """Verifica se o processo está encerrado."""
        return self.state == "Encerrado"

def simulate_processes(n_processes):
    """Simula o ciclo de vida de N processos."""
    processes = [Process(pid) for pid in range(n_processes)]
    while any(not p.is_terminated() for p in processes):
        for process in processes:
            if not process.is_terminated():
                process.transition()
                print(f"Processo {process.pid} está no estado: {process.state}")
        time.sleep(1)  # Atraso para visualização das transições

# Simular 5 processos
simulate_processes(5)
