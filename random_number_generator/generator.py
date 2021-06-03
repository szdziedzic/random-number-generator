class Generator:
    def __init__(self, a=7 ** 5, m=2 ** 31 - 1, x0=1):
        self.a = a
        self.m = m
        self.last_x = x0
        self.next_step = 1

    def generate_number(self):
        number = (self.a * self.last_x) % self.m
        self.last_x = number
        self.next_step = self.next_step + 1
        return number

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
