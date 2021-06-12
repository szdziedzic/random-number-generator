import numpy as np
from random_number_generator.uniform_generator import UniformGenerator


class NormalGenerator:
    def __init__(self, uniform_generator=None):
        if uniform_generator:
            self.uniform_generator = uniform_generator
        else:
            self.uniform_generator = UniformGenerator()

    def generate_number(self):
        u1 = self.uniform_generator.generate_number()
        u2 = self.uniform_generator.generate_number()
        number = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
        return number

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
