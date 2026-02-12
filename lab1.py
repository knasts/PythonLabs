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

        x_n = x_next

    return x_n

def chordal_method(a, b, eps):
    print(f"\n chordal method: a={a}, b={b}, eps={eps}")
    if f(a) * f_deriv2(a) > 0:
        c = a
    else:
        c = b

    if c == a:
        x_n = b
    else:
        x_n = a

    m = min(abs(f_deriv1(a)), abs(f_deriv1(b)))

    n = 0
    while True:
        x_next = x_n - (f(x_n) * (x_n - c)) / (f(x_n) - f(c))
        delta = (1/m) * abs(f(x_next))
        n+=1
        print(f"n = {n}: x = {x_next:.6f}, f(x) = {f(x_next):.6e}, delta = {delta:.6e}")

        if delta < eps: break
        x_n = x_next
    return x_next




if __name__ == "__main__":
    visualize_fx()

    interval = [0, 1]
    #interval1 = [3.5, 4.5]
    precision = 0.001
    #precision1 = 0.00001

    relax_method = relaxation_method(interval[0], interval[1], precision)
    print(f"result of the relaxation method: {relax_method:.6e}")
    #relax_method = relaxation_method(interval[0], interval[1], precision1)
    #print(f"result of the relaxation method: {relax_method:.6e}")

    chord = chordal_method(interval[0], interval[1], precision)
    print(f"result of the chordal method: {chord:.6e}")
    #chord = chordal_method(interval[0], interval[1], precision1)
    #print(f"result of the chordal method: {chord:.6e}")

