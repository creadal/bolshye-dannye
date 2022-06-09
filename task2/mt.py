from multiprocessing import Pool
from factor import factorize


def factorize_mt(numbers):
    count = 0
    for number in numbers:
        count += len(factorize(int(number)))

    return count

if __name__ == '__main__':
    num_threads = 4

    numbers = []
    with open('task2\\numbers.txt', 'r') as file:
        numbers = file.readlines()

    slices = [numbers[i*2000//num_threads:(i+1)*2000//num_threads] for i in range(num_threads)]

    with Pool(num_threads) as pool:
        result = pool.map(factorize_mt, slices)

    print(sum(result))

    '''
    for i in range(8):
        pool.append(Process(target=factorize_mt, args=[i * 250, (i + 1) * 250, result, i]))

    for p in pool:
        p.start()

    for p in pool:
        p.join()

    
    print(sum(result.values()))
    '''