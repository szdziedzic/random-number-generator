from random_number_generator.generator import Generator
from random_number_generator.uniform_generator import UniformGenerator
from random_number_generator.poisson_generator import PoissonGenerator
from random_number_generator.bernoulli_generator import BernoulliGenerator
from random_number_generator.binomial_generator import BinomialGenerator
from random_number_generator.exponential_generator import ExponentialGenerator
from random_number_generator.normal_generator import NormalGenerator
import scipy.stats as sp


def uniform_cdf(a, b, x):
    return (x - a) / (b - a)


def calculate_chi_square_obs(obs: list, exp: list):
    val = 0
    for i in range(len(obs)):
        val = val + ((obs[i] - exp[i]) ** 2) / exp[i]
    return val


def test_bernoulli(generator: BernoulliGenerator, alfa=0.05, n=10000):
    obs = [0, 0]
    exp = [n - n * generator.p, n * generator.p]
    for i in range(len(exp)):
        if exp[i] < 5:
            print(f'exp[{i}] < 5')
            return
    for i in range(n):
        num = generator.generate_number()
        if num == 0:
            obs[0] = obs[0] + 1
        else:
            obs[1] = obs[1] + 1
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=1)
    if chi_square_obs < crit:
        print(f'BERNOULLI TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'BERNOULLI TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_generator(generator: Generator, alfa=0.05, n=10000):
    dist = generator.m / 7
    curr_dist = generator.a
    exp = []
    obs = [0 for i in range(7)]
    for i in range(7):
        next_exp = (uniform_cdf(generator.a, generator.m, curr_dist + dist) - uniform_cdf(generator.a, generator.m,
                                                                                          curr_dist)) * n
        if next_exp < 5:
            print(f'exp[{i}] < 5')
            return
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    values = generator.generate_array(n)
    for value in values:
        curr_ind = 0
        for i in range(7):
            if value < (i + 1) * dist:
                break
            else:
                curr_ind = curr_ind + 1
        obs[curr_ind] = obs[curr_ind] + 1
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=6)
    if chi_square_obs < crit:
        print(f'GENERATOR TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'GENERATOR TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_uniform(generator: UniformGenerator, alfa=0.05, n=10000):
    dist = 1 / 7
    curr_dist = generator.generator.a / generator.generator.m
    exp = []
    obs = [0 for i in range(7)]
    for i in range(7):
        next_exp = (uniform_cdf(generator.generator.a / generator.generator.m, 1, curr_dist + dist) - uniform_cdf(
            generator.generator.a / generator.generator.m, 1,
            curr_dist)) * n
        if next_exp < 5:
            print(f'exp[{i}] < 5')
            return
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    values = generator.generate_array(n)
    for value in values:
        curr_ind = 0
        for i in range(7):
            if value < (i + 1) * dist:
                break
            else:
                curr_ind = curr_ind + 1
        obs[curr_ind] = obs[curr_ind] + 1
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=6)
    if chi_square_obs < crit:
        print(f'UNIFORM TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'UNIFORM TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')
