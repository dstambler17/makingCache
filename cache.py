class Cache:

    num_sets = 0
    num_blocks = 0
    num_bytes = 0
    write_allocate_or_not = 0
    write_through_or_back = 0
    eviction = 0

    def __init__(self, num_sets, num_blocks, num_bytes, write_allocate_or_not, write_through_or_back, eviction):
        self.num_sets = num_sets
        self.num_blocks = num_blocks
        self.num_bytes = num_bytes
        self.write_allocate_or_not = write_allocate_or_not
        self.write_through_or_back = write_through_or_back
        self.eviction = eviction

    cache_array = [num_sets][num_blocks]
    def load(self, ):
    def store(self):
    def get_cycles(self):
