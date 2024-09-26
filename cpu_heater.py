import multiprocessing
import sys

def round_robin_count():
    while True:
        number = 0
        if number >= sys.maxsize:
            number = 0
        else:
            number += 1

if __name__ == "__main__":
    process_count = 1
    print("Heating up the CPU")
    while process_count <= multiprocessing.cpu_count():
        process = multiprocessing.Process(target=round_robin_count)
        process.start()
        process_count += 1
