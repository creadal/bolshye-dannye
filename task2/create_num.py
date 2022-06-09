import numpy as np

with open('numbers.txt', 'w') as file:
    for i in range(2000):
        file.write(str(np.random.randint(0, 2 ** 32, dtype=np.uint32)) + '\n')