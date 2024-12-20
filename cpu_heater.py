import multiprocessing
import sys
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def round_robin_count():
    number = 0
    while True:
        if number >= sys.maxsize:
            number = 0
        else:
            number += 1

def start_processes():
    processes = []
    process_count = 1
    print(Fore.RED + "Heating up the CPU... ", end='', flush=True)  # Keep it on the same line
    while process_count <= multiprocessing.cpu_count():
        process = multiprocessing.Process(target=round_robin_count)
        processes.append(process)
        process.start()
        process_count += 1
    return processes

def stop_processes(processes):
    for process in processes:
        process.terminate()
        process.join()

if __name__ == "__main__":
    processes = []
    toggle = False

    print(Fore.CYAN + "Press Enter to toggle (on/off)...")
    while True:
        input()  # Wait for Enter key to toggle
        if toggle:
            # Stop the processes
            stop_processes(processes)
            print(Fore.GREEN + "\rProcesses stopped.            ")  # Clear line and print stopped message
            time.sleep(1)  # Adding a 1-second delay after stopping processes
        else:
            # Start the processes
            processes = start_processes()
            print(Fore.RED + "\rProcesses started.             ")  # Clear line and print started message
            time.sleep(1)  # Adding a 1-second delay after starting processes

        toggle = not toggle
        # Print a blank line to avoid cluttering
        print("")  # Optional: This line can be removed if you want to keep it even cleaner.