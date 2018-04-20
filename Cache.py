from Block import Block
class Cache:

    num_sets = 0
    num_blocks = 0
    num_bytes = 0
    write_allocate_or_not = 0
    write_through_or_back = 0
    eviction = 0

    #cycles to keep track
    load_hits = 0
    load_miss = 0
    store_hits = 0
    store_miss = 0


    def __init__(self, num_sets, num_blocks, num_bytes, write_allocate_or_not, write_through_or_back, eviction):
        self.num_sets = num_sets
        self.num_blocks = num_blocks
        self.num_bytes = num_bytes
        self.write_allocate_or_not = write_allocate_or_not
        self.write_through_or_back = write_through_or_back
        self.eviction = eviction

    cache_array = [[None for _ in range(num_blocks)] for _ in range(num_sets)]

    def find_fifo(self):
        b2 = self.cache_array[index][1].get_fifo()
        x = 0
        for i in range(self.num_blocks):
            if b2 < self.cache_array[index][i].get_fifo():
                b2 = self.cache_array[index][i].get_fifo()
                x = i
        return x


    def find_lru(self):
        b2 = self.cache_array[index][1].get_lru()
        x = 0
        for i in range(self.num_blocks):
            if b2 < self.cache_array[index][i].get_lru():
                b2 = self.cache_array[index][i].get_lru()
                x = i
        return x


    def load(self, tag, index):
        b1 = Block(tag)
        for i in range(self.num_blocks):
            if(self.cache_array[index][i].get_tag() == tag):
                self.load_hits += 1
                self.cache_array[index][i].reset_lru()
                return
        for i in range(self.num_blocks):
            if(self.cache_array[index][i] == None):
                self.cache_array[index][i] = b1
                self.load_miss += 1
                return
        x = 0
        if self.eviction == 0:
            x = find_fifo()
        elif self.eviction == 1:
            x = find_lru()
        self.cache_array[index][x] == b1
        self.load_miss += 1
        return


        #for set in cache_array:
        #    for item in set:
        #        if item != None:
        #            if item.get_tag() == tag:
        #                self.load_miss
        #                break

        #for set in cache_array:
        #    for item in set:


        myBlock = Block(tag)
        print("hi")

    def store(self, tag, index):
        myBlock = Block(tag)
        print("hello")


    def get_cycles(self):
        total_load = self.load_hits + self.load_miss
        total_store = self.store_hits + self.store_miss
        total_cycles = total_load + total_store
        return total_load, total_store, self.load_hits, self.load_miss, self.store_hits, self.store_miss, total_cycles
