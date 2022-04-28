import os
import time
import mmap
from concurrent.futures import ThreadPoolExecutor
import math


def calc_sum(descriptor):
    uint32_size = 4
    sum = 0

    bytes = descriptor.read(uint32_size)
    while bytes:
        sum += int.from_bytes(bytes, byteorder='big', signed=False)
        bytes = descriptor.read(uint32_size)

    return sum


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

        yield mmap.mmap(descriptor.fileno(), length=length, offset=offset, access=mmap.ACCESS_READ)
    

def st_sum(filename):
    with open(filename, 'rb') as f:
        return calc_sum(f)


def mt_sum(filename):
    sum = 0
    with ThreadPoolExecutor() as executor:
        with open(filename, 'rb') as f:
            for result in executor.map(calc_sum, mmap_file_parts(f, max_workers=executor._max_workers)):
                    sum+=result
        
    return sum


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

    st_result, st_time = measure('st sum', lambda: st_sum(filename))
    mt_result, mt_time = measure('mm mt sum', lambda: mt_sum(filename))
    
    print('Results are the same: %s' % (st_result == mt_result))
    print('acceleration: %f times' % (st_time / mt_time))