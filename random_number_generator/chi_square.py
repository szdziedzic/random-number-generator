from random_number_generator.generator import Generator
from random_number_generator.uniform_generator import UniformGenerator
from random_number_generator.poisson_generator import PoissonGenerator
from random_number_generator.bernoulli_generator import BernoulliGenerator
from random_number_generator.binomial_generator import BinomialGenerator
from random_number_generator.exponential_generator import ExponentialGenerator
from random_number_generator.normal_generator import NormalGenerator
import scipy.stats as sp
from scipy.integrate import quad
import numpy as np
import math


def fill_obs_array(values, dist, obs: list, bins: int, start: float):
    for value in values:
        curr_ind = 0
        for i in range(bins):
            if value <= (i + 1) * dist + start:
                break
            elif curr_ind < bins - 1:
                curr_ind = curr_ind + 1
        obs[curr_ind] = obs[curr_ind] + 1


def uniform_cdf(a, b, x):
    return (x - a) / (b - a)


def exponential_cdf(x, lambda_value):
    return 1 - np.exp(-lambda_value * x)


def standard_normal_pdf(x):
    # box-mueller method generates standard normal distribution
    # so as pdf we take fi(x)
    return np.exp((-(x ** 2)) / 2) / np.sqrt(2 * np.pi)


def calculate_chi_square_obs(obs: list, exp: list):
    val = 0
    for i in range(len(obs)):
        if exp[i] >= 5:
            val = val + ((obs[i] - exp[i]) ** 2) / exp[i]
    return val


def test_bernoulli(generator: BernoulliGenerator, alfa=0.05, n=100000):
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


def test_generator(generator: Generator, alfa=0.05, n=100000, bins=7):
    dist = generator.m / bins
    curr_dist = generator.a
    exp = []
    obs = [0 for i in range(bins)]
    for i in range(bins):
        next_exp = (uniform_cdf(generator.a, generator.m, curr_dist + dist) - uniform_cdf(generator.a, generator.m,
                                                                                          curr_dist)) * n
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    values = generator.generate_array(n)
    fill_obs_array(values, dist, obs, bins, generator.a)
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=bins - 1)
    if chi_square_obs < crit:
        print(f'GENERATOR TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'GENERATOR TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_uniform(generator: UniformGenerator, alfa=0.05, n=100000, bins=7):
    dist = 1 / bins
    curr_dist = generator.generator.a / generator.generator.m
    exp = []
    obs = [0 for i in range(bins)]
    for i in range(bins):
        next_exp = (uniform_cdf(generator.generator.a / generator.generator.m, 1, curr_dist + dist) - uniform_cdf(
            generator.generator.a / generator.generator.m, 1,
            curr_dist)) * n
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    values = generator.generate_array(n)
    fill_obs_array(values, dist, obs, bins, generator.generator.a / generator.generator.m)
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=bins - 1)
    if chi_square_obs < crit:
        print(f'UNIFORM TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'UNIFORM TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_binomial(generator: BinomialGenerator, alfa=0.05, n=100000, bins=7):
    dist = generator.n / bins
    curr_dist = 0
    exp = []
    obs = [0 for i in range(bins)]
    for i in range(bins):
        lower = 0
        if curr_dist != 0:
            lower = int(curr_dist) + 1
        upper = int(curr_dist + dist)
        prob = 0
        for j in range(lower, upper + 1):
            prob = prob + (math.factorial(generator.n) / ((math.factorial(j)) * math.factorial(generator.n - j))) \
                   * (generator.bernoulli_generator.p ** j) \
                   * ((1 - generator.bernoulli_generator.p) ** (generator.n - j))
        exp.append(n * prob)
        curr_dist = curr_dist + dist

    values = generator.generate_array(n)
    fill_obs_array(values, dist, obs, bins, 0)
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=bins - 1)
    if chi_square_obs < crit:
        print(f'BINOMIAL TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'BINOMIAL TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_exponential(generator: ExponentialGenerator, alfa=0.05, bins=7, n=100000):
    values = generator.generate_array(n)
    dist = (max(values) - 0) / bins
    curr_dist = 0
    exp = []
    for i in range(bins):
        next_exp = (exponential_cdf(curr_dist + dist, generator.lambda_value)
                    - exponential_cdf(curr_dist, generator.lambda_value)) * n
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    obs = [0 for i in range(bins)]
    fill_obs_array(values, dist, obs, bins, 0)
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=bins - 1)
    if chi_square_obs < crit:
        print(f'EXPONENTIAL TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'EXPONENTIAL TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_poisson(generator: PoissonGenerator, alfa=0.05, n=100000, bins=7):
    values = generator.generate_array(n)
    dist = (max(values) - 0) / bins
    curr_dist = 0
    exp = []
    for i in range(bins):
        lower = 0
        if curr_dist != 0:
            lower = int(curr_dist) + 1
        upper = int(curr_dist + dist)
        prob = 0
        for j in range(lower, upper + 1):
            prob = prob + ((np.exp(-generator.lambda_value) * generator.lambda_value ** j) / math.factorial(j))
        next_exp = prob * n
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    obs = [0 for i in range(bins)]
    fill_obs_array(values, dist, obs, bins, 0)
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=bins - 1)
    if chi_square_obs < crit:
        print(f'POISSON TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'POISSON TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')


def test_normal(generator: NormalGenerator, alfa=0.05, n=100000, bins = 7):
    values = generator.generate_array(n)
    dist = (max(values) - min(values)) / bins
    curr_dist = min(values)
    exp = []
    for i in range(bins):
        next_exp = quad(standard_normal_pdf, curr_dist, curr_dist + dist)[0] * n
        exp.append(next_exp)
        curr_dist = curr_dist + dist
    obs = [0 for i in range(bins)]
    fill_obs_array(values, dist, obs, bins, min(values))
    chi_square_obs = calculate_chi_square_obs(obs, exp)
    crit = sp.chi2.ppf(q=1 - alfa, df=bins - 1)
    if chi_square_obs < crit:
        print(f'NORMAL TEST PASSED - crit={crit} chi_square_obs={chi_square_obs}')
    else:
        print(f'NORMAL TEST FAILED - crit={crit} chi_square_obs={chi_square_obs}')