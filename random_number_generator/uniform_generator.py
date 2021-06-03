from random_number_generator.generator import Generator


class UniformGenerator:
    def __init__(self, generator=None):
        if not generator:
            self.generator = Generator()
        else:
            self.generator = generator

    def generate_number(self):
        number = self.generator.generate_number()
        number = number / self.generator.m
        return number

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
