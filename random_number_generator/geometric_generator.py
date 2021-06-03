from random_number_generator.bernoulli_generator import BernoulliGenerator


class GeometricGenerator:
    def __init__(self, bernoulli_generator=None, p=0.3):
        if not bernoulli_generator:
            self.bernoulli_generator = BernoulliGenerator(p=p)
        else:
            self.bernoulli_generator = bernoulli_generator

    def generate_number(self):
        number = 1
        while self.bernoulli_generator.generate_number() == 0:
            number = number + 1
        return number

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
