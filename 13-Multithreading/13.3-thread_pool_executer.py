from concurrent.futures import ThreadPoolExecutor
import time

def print_nums(nums):
    time.sleep(1)
    return f'Number :{nums}'

numbers = [1,3,5,7,9,2,4,6,8,0]

with ThreadPoolExecutor(max_workers = 3) as executor:
    results = executor.map(print_nums, numbers)

for result in results:
    print(result)