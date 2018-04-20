from Block import Block
class Cache:

    num_sets = 0
    num_blocks = 0
    num_bytes = 0
    write_allocate_or_not = 0
    write_through_or_back = 0
    eviction = 0
    cache_array = []

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
        self.cache_array = [[None for x in range(num_blocks)] for y in range(num_sets)]

    #def create_array(set, blocks):
        #bNull = Block(-1)
        #array = [[bNull for x in range(set)] for y in range(blocks)]

        #array = []
        #for i in range(set):
        #    block = []
        #    for j in range(blocks):
        #        block.append(bNull)
        #    array.append(block)
        #return array


    #cache_array = create_array(num_sets, num_blocks)
    #cache_array = [[0 for x in range(self.num_sets)] for y in range(self.num_blocks)]

    def get_cache_array(self):
        return self.cache_array

    def find_fifo(self, index):
        b2 = self.cache_array[index][1].get_fifo()
        x = 0
        for i in range(self.num_blocks):
            if b2 < self.cache_array[index][i].get_fifo():
                b2 = self.cache_array[index][i].get_fifo()
                x = i
        return x 


    def find_lru(self, index):
        b2 = 0
        x = 0
        for i in range(self.num_blocks):
            if(self.cache_array[index][i] != None):
                if b2 < self.cache_array[index][i].get_lru():
                    b2 = self.cache_array[index][i].get_lru()
                    x = i
        return x

    #Increment if miss
    def store_is_miss(self, tag, index):
        b = Block(tag)
        pos = 0

        #If you modify cache
        if self.write_allocate_or_not == 1:
            full_set = 1
            for i in range(self.num_blocks):
                if(self.cache_array[index][i] == None):
                    self.cache_array[index][i] = b
                    self.store_miss = self.store_miss + 1
                    full_set = 0
                    pos = i
                    break

            if full_set == 1: #if full,
                if self.eviction == 0:
                    x = find_fifo(index)
                    self.cache_array[index][x] = b
                elif self.eviction == 1:
                    x = self.find_lru(index)
                    self.cache_array[index][x] = b

                if self.cache_array[index][x].get_dirty_bit() == 1:
                    self.load_miss = self.load_miss + 1

        #if you mod memory
        if self.write_through_or_back == 1:
            self.store_miss = self.store_miss + 100 #write to memory

        #if you do dirty bit
        elif self.write_through_or_back == 0:
            item = self.cache_array[index][pos]
            item.set_dirty_bit_true()



    #Increment if store is a hit
    def store_is_hit(self, index, pos):
        self.store_hits = self.store_hits + 1

        if self.write_through_or_back == 0:
            item = self.cache_array[index][pos]
            item.set_dirty_bit_true()


    #Increment counter
    def increment_counters(self, tag, index):
        for item in self.cache_array[index]:
            if item !=None:
                item.increment_lru()
                item.increment_fifo()


    def store(self, tag, index):
        hit = 0
        for i in range(self.num_blocks):
            if(self.cache_array[index][i] != None):
            #if item !=None:
                if(self.cache_array[index][i].get_tag() == tag):
                    hit = 1
                    pos = i
                    self.cache_array[index][i].reset_lru()
                    break

        if hit == 1:
            self.store_is_hit(index, pos)
        else:
            self.store_is_miss(tag, index)

        #increment counters
        self.increment_counters(tag, index)


    def load(self, tag, index):
        b1 = Block(tag)
        for i in range(self.num_blocks):
            if(self.cache_array[index][i] != None):
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
            x = self.find_fifo(index)
        elif self.eviction == 1:
            x = self.find_lru(index)

        if self.cache_array[index][x].get_dirty_bit() == 1:
            self.load_miss += 1
        self.cache_array[index][x] = b1
        self.load_miss += 1
        return


    def get_cycles(self):
        total_load = self.load_hits + self.load_miss
        total_store = self.store_hits + self.store_miss
        total_cycles = total_load + total_store
        return total_load, total_store, self.load_hits, self.load_miss, self.store_hits, self.store_miss, total_cycles
