import multiprocessing
import sys

def intensive_computation():
    number = 0
    while True:
        if number >= sys.maxsize:
            number = 0
        else:
            number += 1
        # Adding more complex calculations
        _ = number ** 2
        _ = number ** 0.5
        _ = number * number

if __name__ == "__main__":
    print("Heating up the CPU")
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        process = multiprocessing.Process(target=intensive_computation)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
