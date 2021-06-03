from random_number_generator.bernoulli_generator import BernoulliGenerator


class BinomialGenerator:
    def __init__(self, bernoulli_generator=None, p=0.3, n=10):
        self.n = n
        if not bernoulli_generator:
            self.bernoulli_generator = BernoulliGenerator(p=p)
        else:
            self.bernoulli_generator = bernoulli_generator

    def generate_number(self):
        number = 0
        for i in range(self.n):
            b = self.bernoulli_generator.generate_number()
            if b == 1:
                number = number + 1

        return number

    def generate_array(self, length: int):
        arr = []
        for i in range(length):
            arr.append(self.generate_number())
        return arr
