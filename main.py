import matplotlib.pyplot as plt
from random_number_generator.generator import Generator

G = Generator()

G_x = []

for i in range(1000000):
    G_x.append(G.generate_number())

plt.hist(G_x)
plt.show()
