from math import exp
from random_number_generator.uniform_generator import UniformGenerator


class PoissonGenerator:
    def __init__(self, uniform_generator=None, lambda_value=4):
        self.lambda_value = lambda_value
        if not uniform_generator:
            self.uniform_generator = UniformGenerator()
        else:
            self.uniform_generator = uniform_generator

    def generate_number(self):
        u = self.uniform_generator.generate_number()
        x = 0
        while u >= exp(-self.lambda_value):
            u = u * self.uniform_generator.generate_number()
            x = x + 1
        return x

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
