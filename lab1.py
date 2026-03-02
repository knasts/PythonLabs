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

def function(x):
    return abs(3 * x ** 2 + 5 * x - 4) + 3

def brute_force(a = 0, b = 1, step = 0.001):
    min_y = 8.0
    x = a
    best_x = x
    while x < b:
        y = function(x)
        if y < min_y:
            min_y = y
            best_x = x
        x += step
    return best_x, min_y


def davis_swann_campey_function(x0, step):
    y0 = function(x0)
    x1 = x0 + step
    y1 = function(x1)
    k = 2
    if y1 > y0:
        step = -step
        x1 = x0 + step
        y1 = function(x1)
        k += 1
        if y1 > y0:
            return sorted([x0 + step, x0 - step]), k
    while True:
        step *= 2
        xn = x1 + step
        yn = function(xn)
        k += 1
        if yn > y1:
            return sorted([x0, xn]), k
        x0, x1 = x1, xn
        y0, y1 = y1, yn


def dichotomy_method(a = 0.0, b = 1.0, eps = 0.001):
    if abs(a - b) < eps:
        return (a + b) / 2.0
    xm = (a + b) / 2.0
    x1 = (a + xm) / 2.0
    x2 = (b + xm) / 2.0
    ym = function(xm)
    y2 = function(x2)
    y1 = function(x1)
    if ym > y2:
        return dichotomy_method(xm, b, eps)
    elif ym > y1:
        return dichotomy_method(a, xm, eps)
    else:
        return dichotomy_method(x1, x2, eps)


def ternary_search(a = 0, b = 1, eps = 0.001):
    while abs(a - b) > eps:
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        if function(m1) < function(m2):
            b = m2
        else:
            a = m1
    return (a + b) / 2.0

def golden_ratio(a, b, step = 0.001):
    ratio = (1 + math.sqrt(5))/2
    x1 = b - (b - a) / ratio
    x2 = a + (b - a) / ratio
    f1 = function(x1)
    f2 = function(x2)
    while abs(a - b) > step:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / ratio
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / ratio
            f2 = function(x2)
    return (a + b) / 2.0

def fibonacci(k):
    n = 0
    n_next = 1
    for i in range(k):
        temp = n
        n = n_next
        n_next = n_next + temp
    return n

def fibonacci_method(a, b, N = 20):
    x1 = a + (fibonacci(N)/fibonacci(N+2)) * (b - a)
    x2 = a + (fibonacci(N+1)/fibonacci(N+2)) * (b - a)
    f1 = function(x1)
    f2 = function(x2)
    for i in range(1, N):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fibonacci(N - i - 1)/fibonacci(N - i + 1)) * (b - a)
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fibonacci(N - i + 2)/fibonacci(N - i + 3)) * (b - a)
            f2 = function(x2)
    return (a + b) / 2.0


def analyze_dsc_steps():
    x0 = [0.8 , 0.2 , 1.0]
    steps = [0.001, 0.01, 0.1 , 1.0]
    for x in x0:
        for step in steps:
            interval, kocf = davis_swann_campey_function(x, step)
            if interval:
                res_interval = f"[{interval[0]:.4f}, {interval[1]:.4f}]"
                print(f"{x:<5}, {step:<5}, {res_interval:<26}, {kocf:<5}")
            else:
                print(f"{x:<5}, {step:<5}, {'not found':<26}, {kocf:<5}")



if __name__ == '__main__':
    visualize_fx()
    analyze_dsc_steps()
