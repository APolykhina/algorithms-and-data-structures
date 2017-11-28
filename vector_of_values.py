class the_vector_of_values:
    def __init__(self, str):
        self.size = len(str)
        self.size_vector = (len(str) - 1) // 8 + 1
        self.vector = bytearray([0] * self.size_vector)
        for i in range(len(str)):
            if str[i] == "1":
                self._set_bit(i)

def _set_bit(self, position):
    self.vector[position // 8] = self.vector[position // 8] | (1 << (7 - (position % 8)))
    
    def _check_bit(self, position):
        return (self.vector[position // 8] & (1 << (7 - (position % 8)))) != 0
    
    def get_vector(self):
        rez = ""
        for i in range(self.size):
            rez = rez + str(int(self._check_bit(i)))
        return rez
    
    def get_bit(self, position):
        return self._check_bit(position)
    
    def get_size(self):
        return self.size