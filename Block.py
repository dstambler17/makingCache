#Kevin Sherman
#Daniel Stambler
#ksherma6@jhu.edu
#dstambl2@jhu.edu

class Block:
    tag = 0
    dirty_bit = 0
    fifo = 0
    lru = 0

    def __init__(self, tag):
        self.tag = tag

    def set_dirty_bit_true(self):
        self.dirty_bit = 1

    def reset_lru(self):
        self.lru = 0

    def get_dirty_bit(self):
        return self.dirty_bit

    def increment_fifo(self):
        self.fifo = self.fifo + 1

    def increment_lru(self):
        self.lru = self.lru + 1

    def get_tag(self):
        return self.tag

    def get_fifo(self):
        return self.fifo

    def get_lru(self):
        return self.lru
