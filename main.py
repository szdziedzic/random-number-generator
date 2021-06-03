import matplotlib.pyplot as plt
import numpy as np
from random_number_generator.generator import Generator
from random_number_generator.uniform_generator import UniformGenerator
from random_number_generator.poisson_generator import PoissonGenerator
from random_number_generator.bernoulli_generator import BernoulliGenerator

LENGTH = 10000

G = Generator()
J = UniformGenerator()
P = PoissonGenerator()
B = BernoulliGenerator()

G_x = G.generate_array(LENGTH)

plt.title('G')
plt.hist(G_x)
plt.show()

J_x = J.generate_array(LENGTH)

plt.title('J')
plt.hist(J_x)
plt.show()

P_x = P.generate_array(LENGTH)

print(np.mean(P_x))
print((np.std(P_x)) ** 2)
plt.title('P')
plt.hist(P_x, bins=max(P_x))
plt.show()

B_x = B.generate_array(LENGTH)
plt.title('B')
plt.hist(B_x)
plt.show()
