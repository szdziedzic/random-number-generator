from random_number_generator.uniform_generator import UniformGenerator


class BernoulliGenerator:
    def __init__(self, uniform_generator=None, p=0.5):
        self.p = p
        if not uniform_generator:
            self.uniform_generator = UniformGenerator()
        else:
            self.uniform_generator = uniform_generator

    def generate_number(self):
        u = self.uniform_generator.generate_number()
        if u < self.p:
            return 0
        return 1

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
