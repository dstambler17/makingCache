import sys
import math
from Cache import Cache

#Checks that command line args are valid
def check_validity_of_args(set, block, byte, w_a, w_t, least_recent):

    #masks to check powers of 2
    set_mask = set - 1
    block_mask = block -1
    byte_mask = byte - 1
    set_result = set & set_mask
    block_result = block & block_mask
    byte_result = byte & byte_mask

    if w_a != 0 and w_a != 1:
        raise ValueError("Improper command line")
        exit(0)
    if w_t != 0 and w_t != 1:
        raise ValueError("Improper command line")
        exit(0)
    if least_recent != 0 and least_recent != 1:
        raise ValueError("Improper command line")
        exit(0)
    if byte < 0 or set_result != 0:
        raise ValueError("Improper command line")
        exit(0)
    if byte < 0 or block_result != 0:
        raise ValueError("Improper command line")
        exit(0)
    if byte < 4 or byte_result != 0:
        raise ValueError("Improper command line")
        exit(0)

def getMemVals(mem, ind, off):
    mem_int = int(mem, 0)
    mem_int = mem_int >> off
    x = 1 << (ind + 1)
    x = x-1
    ind_val = mem_int & x
    tag = mem_int >> ind
    print("tag is: " + str(tag))
    print("ind_val is: " + str(ind_val))
    return ind_val, tag

def readfile(filename, index, offset, myCache):
    with open(filename) as f:
        for line in f:
            input = (str(line)).split(" ")
            s1 = input[0]
            #print(s1)
            mem_address = input[1]
            ind_val, tag = getMemVals(mem_address, index, offset)
            #print(mem_address)
            if s1 == 'l':
                myCache.load(tag, ind_val)
                exit(0)
            elif s1 == 's':
                myCache.store(tag, ind_val)
                exit(0)
            else:
                print ("Something is wrong.")
                exit(0)
    print("Number of stores: " + str(numS))
    print("Number of loads: " + str(numL))

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

    check_validity_of_args(num_sets, num_blocks, num_bytes, write_allocate_or_not, write_through_or_back, eviction)

    #get index and offset
    index = int(math.log(num_sets,2))
    offset = int(math.log(num_bytes,2))
    print(index)
    print(offset)

    simpleCache = Cache(num_sets, num_blocks, num_bytes, write_allocate_or_not, write_through_or_back, eviction)

    readfile(input_file, index, offset, simpleCache)


if __name__ == "__main__":
    main()
