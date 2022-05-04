from multiprocessing import Process, Manager
import os
import time
import mmap
import math
import numpy as np


def calc_sum_process(mmap_params, return_list, idx):
    uint32_size = 4
    s = 0

    with mmap.mmap(**mmap_params) as descriptor:
        bytes = descriptor.read(uint32_size)
        while bytes:
            s += int.from_bytes(bytes, byteorder='big', signed=False)
            bytes = descriptor.read(uint32_size)

    return_list[idx] = s


def mmap_file_parts(descriptor, max_workers):
    bytes_total = os.stat(filename).st_size
    page_size = mmap.ALLOCATIONGRANULARITY
    pages_total = math.ceil(bytes_total / page_size)
    pages_per_worker = math.ceil(pages_total / max_workers)

    bytes_per_worker = page_size*pages_per_worker
    for i in range(max_workers):
        offset = i*pages_per_worker*page_size
        if offset + bytes_per_worker < bytes_total:
            length = bytes_per_worker
        else:
            length = bytes_total - offset

        yield i, {'fileno': descriptor.fileno(), 'length': length, 'offset': offset, 'access': mmap.ACCESS_READ}


def mt_sum(filename):
    num_workers = 8

    pool = []
    manager = Manager()
    result = manager.dict()
    with open(filename, 'rb') as f:
        for i, mmap_param in mmap_file_parts(f, 8):
            p = Process(target=calc_sum_process, args=(mmap_param, result, i))
            pool.append(p)
            pool[-1].start()

        for process in pool:
            process.join()
    
    return sum(result.values())
    

def st_sum(filename):
    uint32_size = 4
    s = 0
    with open(filename, 'rb') as f:
        bytes = f.read(uint32_size)
        while bytes:
            s += int.from_bytes(bytes, byteorder='big', signed=False)
            bytes = f.read(uint32_size)

    return s


def measure(label, func):
    print('Measuring %s' % label)
    start_time = time.time()
    result = func()
    time_score = (time.time() - start_time)
    print("Time: %.2f seconds" % (time_score))
    print("Result: %d" % result)
    return result, time_score


if __name__ == '__main__':
    filename = 'numbers.bin'

    mt_result, mt_time = measure('mm mt sum', lambda: mt_sum(filename))
    st_result, st_time = measure('st sum', lambda: st_sum(filename))
    
    print('Results are the same: %s' % (st_result == mt_result))
    print('acceleration: %f times' % (st_time / mt_time))
