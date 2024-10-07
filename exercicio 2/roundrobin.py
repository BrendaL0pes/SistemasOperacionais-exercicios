from collections import deque

def round_robin(processes, burst_times, quantum):
    n = len(processes)
    remaining_times = burst_times[:]  # Cópia dos tempos de burst
    waiting_times = [0] * n  # Tempo de espera de cada processo
    turnaround_times = [0] * n  # Tempo de retorno (turnaround time)
    
    queue = deque(processes)  # Fila de processos
    time = 0  # Relógio do tempo

    while queue:
        current_process = queue.popleft()
        idx = processes.index(current_process)

        if remaining_times[idx] > quantum:
            # Executa o processo pelo quantum de tempo
            time += quantum
            remaining_times[idx] -= quantum
            # Coloca de volta na fila se ainda tiver tempo de execução
            queue.append(current_process)
        else:
            # Executa o processo pelo tempo restante
            time += remaining_times[idx]
            waiting_times[idx] = time - burst_times[idx]
            remaining_times[idx] = 0

        # Atualiza o turnaround time (tempo de término - tempo de início)
        turnaround_times[idx] = waiting_times[idx] + burst_times[idx]

    # Exibe os resultados
    print("Processo\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

# Exemplo de uso
processes = ['P1', 'P2', 'P3', 'P4']
burst_times = [5, 8, 12, 6]
quantum = 4

round_robin(processes, burst_times, quantum)
