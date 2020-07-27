import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Distribution:
    def draw(self):
        sns.distplot(self.calculate())
        plt.show()

    def summarize(self):
        result = self.calculate()
        print(f"Min =  {np.min(result)}")
        print(f"Max = {np.max(result)}")
        print(f"Mean = {np.mean(result)}")
        print(f"St. Deviation = {np.std(result)}")


class Normal(Distribution):
    def __init__(self, mean: float, std: float, size: int):
        self.mean = mean
        self.std = std
        self.size = size

    def calculate(self):
        return np.random.normal(self.mean, self.std, self.size)


class Poisson(Distribution):
    def __init__(self, lambda_: float, size):
        self.lambda_ = lambda_
        self.size = size

    def calculate(self):
        return np.random.poisson(self.lambda_, self.size)


class Binomial(Distribution):
    def __init__(self, n: int, p: float, size: int):
        self.n = n
        self.p = p
        self.size = size

    def calculate(self):
        return np.random.binomial(self.n, self.p, self.size)
