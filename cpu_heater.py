import multiprocessing
import sys
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def round_robin_count():
    number = 0
    while True:
        number = (number + 1) % sys.maxsize

def start_processes():
    processes = []
    process_count = 1
    print(Fore.RED + "Heating up the CPU... ", end='', flush=True)  # Keep it on the same line
    try:
        while process_count <= multiprocessing.cpu_count():
            process = multiprocessing.Process(target=round_robin_count)
            processes.append(process)
            process.start()
            process_count += 1
    except Exception as e:
        print(Fore.RED + f"Error starting processes: {e}")
        stop_processes(processes)
    return processes

def stop_processes(processes):
    for process in processes:
        process.terminate()
        process.join()