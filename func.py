def rfile(filename):
    numS = 0
    numL = 0
    with open(filename) as f:
        for line in f:
            s1 = line[0];
            print(s1)
            if s1 == 'l':
                numL = numL + 1
                print ("This is a load.")
            elif s1 == 's':
                numS = numS + 1
                print ("This is a store.")
            else:
                print ("Something is wrong.")
    print("Number of stores: " + str(numS))
    print("Number of loads: " + str(numL))


def bitManip(mem, ind, off):
    mem_int = int(mem, 0)
    mem_int = mem_int >> off
    x = 1 << (ind + 1)
    x = x-1
    ind_val = mem_int & x
    tag = mem_int >> ind
    print("tag is: " + str(tag))
    print("ind_val is: " + str(ind_val))



def main():
    filename = "gcc.trace"
    rfile(filename)

if __name__ == "__main__":
    main()
