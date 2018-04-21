#Kevin Sherman
#Daniel Stambler
#ksherma6@jhu.edu
#dstambl2@jhu.edu

import sys
import math
from Cache import Cache

#Checks that command line args are valid
def check_validity_of_args(set, block, byte, w_a, w_t, least_recent, input_file):

    #masks to check powers of 2
    set_mask = set - 1
    block_mask = block -1
    byte_mask = byte - 1
    set_result = set & set_mask
    block_result = block & block_mask
    byte_result = byte & byte_mask

    if w_a != 0 and w_a != 1:
        raise ValueError("Improper command line arg")
        exit(0)
    if w_t != 0 and w_t != 1:
        raise ValueError("Improper command line arg")
        exit(0)
    if least_recent != 0 and least_recent != 1:
        raise ValueError("Improper command line arg")
        exit(0)
    if w_a == 0 and w_t == 0:
        raise ValueError("Improper command line arg")
        exit(0)
    if byte < 0 or set_result != 0:
        raise ValueError("Improper command line arg")
        exit(0)
    if byte < 0 or block_result != 0:
        raise ValueError("Improper command line arg")
        exit(0)
    if byte < 4 or byte_result != 0:
        raise ValueError("Improper command line arg")
        exit(0)
    file_check = input_file.split(".")
    if file_check[1] != "trace":
        raise ValueError("Improper command line arg")
        exit(0)

def getMemVals(mem, ind, off):
    mem_int = int(mem, 0)
    mem_int = mem_int >> off
    x=0
    x = 1 << (ind)
    x -= 1
    ind_val = mem_int & x
    tag = mem_int >> ind
    return ind_val, tag

def readfile(filename, index, offset, myCache):
    with open(filename) as f:
        for line in f:
            input = (str(line)).split(" ")
            s1 = input[0]
            mem_address = input[1]
            ind_val, tag = getMemVals(mem_address, index, offset)
            if s1 == 'l':
                myCache.load(tag, ind_val)
            elif s1 == 's':
                myCache.store(tag, ind_val)
            else:
                raise ValueError("Load and Save must be l or s")
                exit(0)

def main():
    if len(sys.argv) != 8:
        raise ValueError("Too many or too few arguments")
        exit(0)
    num_sets = int(sys.argv[1])
    num_blocks = int(sys.argv[2])
    num_bytes = int(sys.argv[3])
    write_allocate_or_not = int(sys.argv[4])
    write_through_or_back = int(sys.argv[5])
    eviction = int(sys.argv[6])
    input_file = sys.argv[7]

    check_validity_of_args(num_sets, num_blocks, num_bytes, write_allocate_or_not, write_through_or_back, eviction, input_file)

    #get index and offset
    index = int(math.log(num_sets,2))
    offset = int(math.log(num_bytes,2))

    simpleCache = Cache(num_sets, num_blocks, num_bytes, write_allocate_or_not, write_through_or_back, eviction)
    readfile(input_file, index, offset, simpleCache)

    total_load, total_store, load_hits, load_miss, store_hits, store_miss, total_cycles = simpleCache.get_cycles()
    print("Total loads: " + str(total_load))
    print("Total stores: " + str(total_store))
    print("Load hits: " + str(load_hits))
    print("Load misses: " + str(load_miss))
    print("Store hits: " + str(store_hits))
    print("Store misses: " + str(store_miss))
    print("Total cycles: " + str(int(total_cycles)))

if __name__ == "__main__":
    main()
