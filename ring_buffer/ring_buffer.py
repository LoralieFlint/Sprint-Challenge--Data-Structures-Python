class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = list()
        self.capicity_tracker = capacity

 
    def append(self, item):
        if self.capacity > 0:
            self.buffer.append(item)
            self.capacity -= 1
        
        elif self.capacity == 0:
            self.capacity = self.capicity_tracker * -1
            self.buffer[self.capacity] = item
            self.capacity += 1

        elif self.capacity < 0:
            self.buffer[self.capacity] = item
            self.capacity += 1


    def get(self):
      return self.buffer

buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer)
