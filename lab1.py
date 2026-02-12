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
    m2 = max(f_deriv1_a, f_deriv1_b)

    tau = 2 / (m2 + m1)
    x_n = (a+b) / 2

    for i in range(1, max_iter+1):
        x_next = x_n + tau * f(x_n)
        delta = abs(x_next - x_n)
        print(f"n = {i}: x = {x_next:.6f}, f(x) = {f(x_next):.6e}, delta = {delta:.6e}")

        if delta < eps:
            return x_next

        x_n = x_next

    return x_n

def chordal_method(a, b, eps, max_iter=100):
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
    for i in range(1, max_iter+1):
        x_next = x_n - (f(x_n) * (x_n - c)) / (f(x_n) - f(c))
        delta = (1/m) * abs(f(x_next))
        print(f"n = {i}: x = {x_next:.6f}, f(x) = {f(x_next):.6e}, delta = {delta:.6e}")

        if delta < eps: break
        x_n = x_next
    return x_next

def visualize_system():
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    x1, y1 = np.meshgrid(x, y)

    f1 = np.sin(x1 - y1) - x1 * y1 + 1
    f2 = x1**2 - y1**2 - 0.75
    plt.figure(figsize=(8, 5))
    plt.contour(x1, y1, f1, levels = [0], colors='pink', linewidths=2)
    plt.contour(x1, y1, f2, levels=[0], colors='violet', linewidths=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, linestyle=':', alpha=0.8)
    plt.axhline(0, color='blue', linewidth=1, linestyle='--')
    plt.axvline(0, color='blue', linewidth=1, linestyle='--')

    plt.show()

def newton_method_system(x0, y0, eps = 0.01):
    print(f"\n solving system")
    curr_x, curr_y = x0, y0

    n = 0
    while True:
        f1 = np.sin(curr_x - curr_y) - curr_x * curr_y + 1
        f2 = curr_x ** 2 - curr_y ** 2 - 0.75
        func = np.array([f1, f2])

        w11 = math.cos(curr_x - curr_y) - curr_y
        w12 = -math.cos(curr_x - curr_y) - curr_x
        w21 = 2 * curr_x
        w22 = -2 * curr_y
        w = np.array([[w11, w12], [w21, w22]])

        try:
            delta = np.linalg.solve(w, -func)
        except np.linalg.LinAlgError:
            print(f"error in newton method")
            return None

        curr_x = curr_x + delta[0]
        curr_y = curr_y + delta[1]
        n += 1

        err = max(abs(delta))
        print(f"n = {n}, x = {curr_x}, y = {curr_y}, err = {err}")

        if err < eps:
            break

    return curr_x, curr_y


if __name__ == "__main__":
    visualize_fx()

    interval = [0, 1]
    interval_system = [0.8, 0.5]
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
    visualize_system()
    newton_method_system(interval_system[0], interval_system[1])

