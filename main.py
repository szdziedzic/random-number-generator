import matplotlib.pyplot as plt
# import numpy as np
from random_number_generator.generator import Generator
from random_number_generator.uniform_generator import UniformGenerator
from random_number_generator.poisson_generator import PoissonGenerator
from random_number_generator.bernoulli_generator import BernoulliGenerator
from random_number_generator.binomial_generator import BinomialGenerator
from random_number_generator.geometric_generator import GeometricGenerator

LENGTH = 10000

G = Generator()
J = UniformGenerator()
P = PoissonGenerator()
B = BernoulliGenerator(p=0.3)
D = BinomialGenerator(p=0.5, n=20)
W = GeometricGenerator()

G_x = G.generate_array(LENGTH)

plt.title('G')
plt.hist(G_x)
plt.show()

J_x = J.generate_array(LENGTH)

plt.title('J')
plt.hist(J_x)
plt.show()

P_x = P.generate_array(LENGTH)
# print(np.mean(P_x))
# print((np.std(P_x)) ** 2)
plt.title('P')
plt.hist(P_x, bins=max(P_x))
plt.show()

B_x = B.generate_array(LENGTH)
plt.title('B')
plt.hist(B_x)
plt.show()

D_x = D.generate_array(LENGTH)
plt.title('D')
plt.hist(D_x, bins=max(D_x))
plt.show()

W_x = W.generate_array(LENGTH)
plt.title('W')
plt.hist(W_x, bins=max(W_x))
plt.show()
