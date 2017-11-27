class the_vector_of_values:
    def __init__(self, str):
        self.vector = bytearray()
        self.size = len(str)
        if self.size % 8 == 0:
            for i in range(self.size // 8):
                self.vector.append(0)
                for j in range(8):
                    if str[i*8 + j] == "1":
                        self.vector[i] = self._set_bit(self.vector[i], j)
        else:
            for i in range(self.size // 8 + 1):
               self.vector.append(0)
               if i != self.size // 8:
                   for j in range(8):
                       if str[i * 8 + j] == "1":
                           self.vector[i] = self._set_bit(self.vector[i], j)
               else:
                   for j in range(self.size - 8*(self.size // 8)):
                       if str[8*(self.size // 8) + j] == "1":
                           self.vector[i] = self._set_bit(self.vector[i], j)

    def _set_bit(self, value, position):
        return value | (1 << position)

    def _check_bit(self,value, position):
        return (value & (1 << position)) != 0

    def get_vector(self):
        rez = ""
        if self.size % 8 == 0:
            for i in range(self.size // 8):
                for j in range(8):
                    rez = rez + str(int(self._check_bit(self.vector[i], j)))
        else:
            for i in range(self.size // 8 + 1):
                if i != (self.size //8):
                    for j in range(8):
                        rez = rez + str(int(self._check_bit(self.vector[i], j)))
                else:
                    for j in range(self.size - 8*(self.size // 8)):
                        rez = rez + str(int(self._check_bit(self.vector[i], j)))
        return rez

    def get_bit(self, position):
        return self._check_bit(self.vector[position // 8], position - (position // 8)*8)

    def get_size(self):
        return self.size