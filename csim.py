import sys

def check_validity_of_args(set, block, byte, w_a, w_t, least_recent):
    if w_a < 0 or w_a > 1:
        raise ValueError("blech")
        exit(0)
    if w_t < 0 or w_t > 1:
        raise ValueError("blech")
        exit(0)
    if least_recent < 0 or least_recent >1:
        raise ValueError("blech")
        exit(0)
def main():
    if len(sys.argv) != 8:
        raise ValueError("Too many or too few arguments")
        exit(0)
    num_sets = sys.argv[1]
    num_blocks = sys.argv[2]
    num_bytes = sys.argv[3]
    write_allocate = sys.argv[4]
    write_through = sys.argv[5]
    least_recent = sys.argv[6]
    input_file = sys.argv[7]

    #check_validity_of_args(num_sets, num_blocks, num_bytes, write_allocate, write_through, least_recent)



if __name__ == "__main__":
    main()
