import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2 ** x - 4 * x


def f_deriv1(x): #first derivative
    return 2 ** x * math.log(2) - 4


def f_deriv2(x):
    return 2 ** x * (math.log(2) ** 2)

def visualize_fx():
    x = np.linspace(-0.5, 5, 400)
    y = 2 ** x - 4 * x

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color = 'purple', linewidth = 2)
    plt.axhline(0, color='blue', linewidth=1, linestyle='--')
    plt.axvline(0, color='blue', linewidth=1, linestyle='--')

    plt.show()

if __name__ == "__main__":
    visualize_fx()

