import math
import numpy as np
import matplotlib.pyplot as plt

def visualize_fx():
    x = np.linspace(-1, 2, 200)
    y = abs(3 * x **2 + 5 * x - 4) + 3

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color = 'purple', linewidth = 2)
    plt.axhline(0, color='black', linewidth=1, linestyle='--')
    plt.axvline(0, color='black', linewidth=1, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axvline(1, color='blue', linewidth=1, linestyle='--')

    plt.grid(True, linestyle=':', alpha=0.8)

    plt.show()

def first_derivative(x):
    return np.sign(3*x**2 + 5*x - 4) * (6*x + 5)

def second_derivative(x):
    return 6 * np.sign(3 * x ** 2 + 5 * x - 4)

def function(x):
    return abs(3 * x ** 2 + 5 * x - 4) + 3

def brute_force():
    min_y = 8.0
    step = 0.001
    x = 0
    best_x = x
    while x < 1:
        y = function(x)
        if y < min_y:
            min_y = y
            best_x = x
        x += step
    return best_x, min_y


def davis_swann_campey_function(step = 0.001):
    x0 = 0.8

    while True:
        x1 = x0 - step
        x2 = x0 + step
        y0 = function(x0)
        y1 = function(x1)
        y2 = function(x2)
        if y1 >= y0 and y2 >= y0:
            return x1, x2
        elif y1 < y0 and y2 < y0:
            return -1
        elif y1 >= y0 and y0 >= y2:
            while y2 < y0:
                x1 = x0
                x0 = x2
                step *= 2
                x2 = x0 + step
                y0 = function(x0)
                y2 = function(x2)
            return x1, x2
        else:
            while y1 < y0:
                x2 = x0
                x0 = x1
                step *= 2
                x1 = x0 - step
                y0 = function(x0)
                y1 = function(x1)
            return x1, x2

def dichotomy_method(a = 0, b = 1):
    eps = 0.001
    if abs(a - b) < eps:
        return (a + b) / 2.0
    xm = float (a + b) / 2.0
    x1 = (a + xm) / 2.0
    x2 = (b + xm) / 2.0
    ym = function(xm)
    y1 = function(x1)
    y2 = function(x2)
    if ym > y2:
        return dichotomy_method(xm, b)
    elif ym > y1:
        return dichotomy_method(a, xm)
    elif ym < y1 and ym < y2:
        return dichotomy_method(x1, x2)






if __name__ == '__main__':
    visualize_fx()
    print(brute_force())
    step = 0.001
    step1 = 0.01
    step2 = 0.1
    step3 = 1

    print(davis_swann_campey_function(step))
