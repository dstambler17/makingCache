class Block:
    tag = 0
    dirty_bit = 0
    time_in_cell = 0

    def __init__(self, tag):
        self.tag = tag

    def set_dirty_bit_true(self):
        self.dirty_bit = 1

    def reset_counter(self):
        self.time_in_cell = 0

    def get_dirty_bit(self):
        return self.dirty_bit

    def increment_time(self):
        self.time_in_cell = self.time_in_cell + 1

    def get_tag(self):
        return self.tag
