import math
import time
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

def brute_force(a, b, step):
    kocf = 0
    min_y = 8.0
    x = a
    best_x = x
    while x < b:
        y = function(x)
        kocf += 1
        if y < min_y:
            min_y = y
            best_x = x
        x += step
    return best_x, kocf


def davis_swann_campey_function(x0, step):
    y0 = function(x0)
    x1 = x0 + step
    y1 = function(x1)
    kocf = 2
    if y1 > y0:
        step = -step
        x1 = x0 + step
        y1 = function(x1)
        kocf += 1
        if y1 > y0:
            return sorted([x0 + step, x0 - step]), kocf
    while True:
        step *= 2
        xn = x1 + step
        yn = function(xn)
        kocf += 1
        if yn > y1:
            return sorted([x0, xn]), kocf
        x0, x1 = x1, xn
        y0, y1 = y1, yn


def dichotomy_method(a, b, eps ):
    curr_kocf = 0
    if abs(a - b) < eps:
        return (a + b) / 2.0, 0
    xm = (a + b) / 2.0
    x1 = (a + xm) / 2.0
    x2 = (b + xm) / 2.0
    ym = function(xm)
    y2 = function(x2)
    y1 = function(x1)
    curr_kocf += 3
    if ym > y2:
        res, kocf = dichotomy_method(xm, b, eps)
        return res, kocf + curr_kocf
    elif ym > y1:
        res, kocf = dichotomy_method(a, xm, eps)
        return res, kocf + curr_kocf
    else:
        res, kocf = dichotomy_method(x1, x2, eps)
        return res, kocf + curr_kocf


def ternary_search(a, b, eps = 0.001):
    kocf = 0
    while abs(a - b) > eps:
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        if function(m1) < function(m2):
            b = m2
        else:
            a = m1
        kocf += 2
    return (a + b) / 2.0, kocf

def golden_ratio(a, b, step = 0.001):
    kocf = 0
    ratio = (1 + math.sqrt(5))/2
    x1 = b - (b - a) / ratio
    x2 = a + (b - a) / ratio
    f1 = function(x1)
    f2 = function(x2)
    kocf += 2
    while abs(a - b) > step:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / ratio
            f1 = function(x1)
            kocf += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / ratio
            f2 = function(x2)
            kocf += 1
    return (a + b) / 2.0, kocf

def fibonacci(k):
    n = 0
    n_next = 1
    for i in range(k):
        temp = n
        n = n_next
        n_next = n_next + temp
    return n

def fibonacci_method(a, b, N):
    kocf = 0
    x1 = a + (fibonacci(N)/fibonacci(N+2)) * (b - a)
    x2 = a + (fibonacci(N+1)/fibonacci(N+2)) * (b - a)
    f1 = function(x1)
    f2 = function(x2)
    kocf += 2
    for i in range(1, N):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fibonacci(N - i - 1)/fibonacci(N - i + 1)) * (b - a)
            f1 = function(x1)
            kocf += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fibonacci(N - i )/fibonacci(N - i + 1)) * (b - a)
            f2 = function(x2)
            kocf += 1
    return (a + b) / 2.0, kocf


def analyze_dsc_steps():
    x0 = [0.2 , 0.7 , 0.9]
    steps = [0.001, 0.01, 0.1 , 1.0]
    print("dcs analysis:")
    print(f"{'x0':<5}, {'eps':<5}, {'interval':<18}, {'kocf':<5}")
    for x in x0:
        for step in steps:
            interval, kocf = davis_swann_campey_function(x, step)
            if interval:
                res_interval = f"[{interval[0]:.4f}, {interval[1]:.4f}]"
                print(f"{x:<5}, {step:<5}, {res_interval:<18}, {kocf:<5}")
            else:
                print(f"{x:<5}, {step:<5}, {'not found':<18}, {kocf:<5}")

def measure_performance(x1, x2, eps, method):
    iterations = 10000
    start = time.perf_counter()
    res = 0
    kocf = 0
    for i in range(iterations):
        res, kocf = method(x1, x2, eps)
    end = time.perf_counter()
    average_time = ((end - start)/iterations) * 1000000
    return res, kocf, average_time


def compare_methods():
    x1 = 0.0
    x2 = 1.0
    x1_dsc = 0.445
    x2_dsc = 0.637
    eps = [0.001, 0.01, 0.1 , 1.0]
    N = [3, 6, 10]
    methods = [dichotomy_method, ternary_search, golden_ratio, brute_force, fibonacci_method]
    print(f"\n{'method':<17}, {'result':<8}, {'eps':<5}, {'kocf':<4}, {'time':<8}")
    for ep in eps:
        print(f"eps: ", ep)
        res1, k1, t1 = measure_performance(x1, x2, ep, dichotomy_method)
        print(f"dichotomy        , {res1:<8.5f}, {ep:<5}, {k1:<4}, {t1:<8.2f}")
        res2, k2, t2 = measure_performance(x1, x2, ep, ternary_search)
        print(f"ternary search   , {res2:<8.5f}, {ep:<5}, {k2:<4}, {t2:<8.2f}")
        res3, k3, t3 = measure_performance(x1, x2, ep, golden_ratio)
        print(f"golden ratio     , {res3:<8.5f}, {ep:<5}, {k3:<4}, {t3:<8.2f}")
        res4, k4, t4 = measure_performance(x1, x2, ep, brute_force)
        print(f"brute force      , {res4:<8.5f}, {ep:<5}, {k4:<4}, {t4:<8.2f}")
    for n in N:
        res5, k5, t5 = measure_performance(x1, x2, n, fibonacci_method)
        print(f"fibonacci method , {res5:<8.5f}, n={n:<3}, {k5:<4}, {t5:<8.2f}")
    print(f"\n{'using dsc refined interval':<60}")
    res1, k1, t1 = measure_performance(x1_dsc, x2_dsc, eps[0], dichotomy_method)
    print(f"dichotomy       , {res1:<8.5f}, {eps[0]:<4}, {k1:<3}, {t1:<8.2f}")
    res2, k2, t2 = measure_performance(x1_dsc, x2_dsc, eps[0], ternary_search)
    print(f"ternary search  , {res2:<8.5f}, {eps[0]:<4}, {k2:<3}, {t2:<8.2f}")
    res3, k3, t3 = measure_performance(x1_dsc, x2_dsc, eps[0], golden_ratio)
    print(f"golden ratio    , {res3:<8.5f}, {eps[0]:<4}, {k3:<3}, {t3:<8.2f}")
    res4, k4, t4 = measure_performance(x1_dsc, x2_dsc, eps[0], brute_force)
    print(f"brute force     , {res4:<8.5f}, {eps[0]:<4}, {k4:<3}, {t4:<8.2f}")
    res5, k5, t5 = measure_performance(x1_dsc, x2_dsc, N[2], fibonacci_method)
    print(f"fibonacci method, {res5:<8.5f}, n={N[2]:<3}, {k5:<3}, {t5:<8.2f}")


if __name__ == '__main__':
    visualize_fx()
    analyze_dsc_steps()
    compare_methods()

