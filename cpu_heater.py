import multiprocessing
import sys
import time  # This is now used for adding delays

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
    print("Heating up the CPU")
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

    while True:
        input("Press Enter to toggle (on/off)...")
        if toggle:
            # Stop the processes
            stop_processes(processes)
            print("Processes stopped.")
            time.sleep(1)  # Adding a 1-second delay after stopping processes
        else:
            # Start the processes
            processes = start_processes()
            print("Processes started.")
            time.sleep(1)  # Adding a 1-second delay after starting processes

        toggle = not toggle
