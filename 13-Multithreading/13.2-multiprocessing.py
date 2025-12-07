import multiprocessing
import time

def sq_nums():
    for i in range(4):
        time.sleep(1)
        print(f'Square {i*i}', flush=True)
    
def cub_nums():
    for i in range(4):
        time.sleep(1.5)
        print(f'Cube {i*i*i}', flush=True)


if __name__ == "__main__":
    
    # create processes
    p1 = multiprocessing.Process(target=sq_nums)
    p2 = multiprocessing.Process(target=cub_nums)
    t = time.time()
    # start the process
    p1.start()
    p2.start()

    # wait for processes to complete
    p1.join()
    p2.join()
    

    time_taken = time.time() - t
    print(time_taken)