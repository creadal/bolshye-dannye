from os import urandom
from tqdm import tqdm

bin_file = open('numbers.bin', 'ab')

num_bytes = 2 * 1024 ** 3
word_length = 1024

for i in tqdm(range(num_bytes // word_length)):
    bin_file.write(urandom(word_length))

bin_file.close()
