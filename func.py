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

def main():
    filename = "gcc.trace"
    rfile(filename)

if __name__ == "__main__":
    main()
