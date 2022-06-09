from dask.distributed import Client
import dask.dataframe as dd
import pandas as pd
from time import time

from factor import factorize

def factorizer(df):
    return df.apply(lambda n: len(factorize(n)))

if __name__ == "__main__":
    client = Client(n_workers=4, threads_per_worker=2, processes=True, memory_limit='4GB')
    client

    now = time()

    numbers = {'number': []}
    with open('C:\\Users\\user\\Desktop\\bolshye dannye\\task2\\numbers.txt', 'r') as file:
        line = file.readline()
        while line != '':
            numbers['number'].append(int(line))
            line = file.readline()

    df = pd.DataFrame(numbers)
    dfc = dd.from_pandas(df, npartitions=10)
    res_fin = dfc['number'].map_partitions(factorizer, meta=(None, 'int32'))
    print(res_fin.sum().compute())
    print("time elapsed: %fs" % (time() - now))