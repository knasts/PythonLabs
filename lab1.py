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
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, linestyle=':', alpha=0.8)

    plt.show()

def relaxation_method(a, b, eps, max_iter=100):
    print(f"\n relaxation method: a={a}, b={b}, eps={eps}")
    f_deriv1_a = abs(f_deriv1(a))
    f_deriv1_b = abs(f_deriv1(b))
    m1 = min(f_deriv1_a, f_deriv1_b)
    M1 = max(f_deriv1_a, f_deriv1_b)

    tau = 2 / (M1 + m1)
    x_n = (a+b) / 2

    for i in range(1, max_iter+1):
        x_next = x_n + tau * f(x_n)
        delta = abs(x_next - x_n)
        print(f"n = {i}: x = {x_next:.6f}, f(x) = {f(x_next):.6e}, delta = {delta:.6e}")
        if delta < eps:
            return x_next
        return x_n


if __name__ == "__main__":
    visualize_fx()

    interval = [0, 1]
    precision = 0.001

    relax_method = relaxation_method(interval[0], interval[1], precision)
    print(f"relaxation method: {relax_method}")
