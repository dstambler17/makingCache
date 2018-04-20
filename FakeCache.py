from Block import Block
class FakeCache:

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

    def load(self, tag, index):
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

    def store_miss(tag, index):

    def store_hit(tag, index):
        self.store_hits = self.store_hits + 1

    def increment_counters(tag, index):
        for item in self.cache_array[index]:
            if item !=None:
                item.increment_lru()
                item.increment_fifo()

    def store(self, tag, index):
        hit = 0
        for item in self.cache_array[index]:
            if item !=None:
                if item.get_tag() == tag:
                    hit = 1
                    item.reset_lru()
                    break

        if hit == 1:
            store_hit(tag, index)
        else:
            store_miss(tag, index)

        myBlock = Block(tag)
        #increment counters
        increment_counters(tag, index)

        print("hello")


    def get_cycles(self):
        total_load = self.load_hits + self.load_miss
        total_store = self.store_hits + self.store_miss
        total_cycles = total_load + total_store
        return total_load, total_store, self.load_hits, self.load_miss, self.store_hits, self.store_miss, total_cycles
