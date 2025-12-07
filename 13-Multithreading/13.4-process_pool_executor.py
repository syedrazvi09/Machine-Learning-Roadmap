from concurrent.futures import ProcessPoolExecutor
import time

def sq_nums(nums):
    time.sleep(2)
    return f'Square: {nums * nums}'

numbers = [2, 4, 6, 8, 11, 42, 5, 7]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sq_nums, numbers)

    for result in results:
        print(result)