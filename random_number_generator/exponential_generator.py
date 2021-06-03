import numpy as np
from random_number_generator.uniform_generator import UniformGenerator


class ExponentialGenerator:
    def __init__(self, uniform_generator=None, lambda_value=4):
        self.lambda_value = lambda_value
        if not uniform_generator:
            self.uniform_generator = UniformGenerator()
        else:
            self.uniform_generator = uniform_generator

    def generate_number(self):
        u = self.uniform_generator.generate_number()
        return -np.log(1 - u) / self.lambda_value

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
