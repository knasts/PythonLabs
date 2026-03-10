import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t0, tk, y0 = 0.0, 0.9, 0.0

def func(t, y):
    if abs(y) < 1e-9:
        return np.sqrt(2)
    return (t / y) * ((2 - t) / (1 - t)**2)

def runge_kutta4(t, u, h):
    k1 = func(t, u)
    k2 = func(t + 0.5*h, u + 0.5*h*k1)
    k3 = func(t + 0.5*h, u + 0.5*h*k2)
    k4 = func(t + h, u + h*k3)
    return u + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

def implicit_runge_kutta4(t, u, h, eps = 1e-9):
    u_n = u + h * func(t, u)
    t_n = t + h
    for _ in range(10):
        k1 = func(t_n, u_n)
        k2 = func(t_n - 0.5 * h, u_n - 0.5 * h * k1)
        k3 = func(t_n - 0.5 * h, u_n - 0.5 * h * k2)
        k4 = func(t_n, u_n - h * k3)
        u_new = u + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)
        if abs(u_new - u_n) < eps: break
        u_n = u_new
    return u_n

def runge_kutta_fehlberg(t, u, h):
    k1 = 2 * func(t, u)
    k2 = func(t + 0.5*h, u + 0.5*h*k1)
    k3 = func(t + 3/8*h, u + (3/32*k1 + 9/32*k2)*h)
    k4 = func(t + 12/13*h, u + (1932/2197*k1 - 7200/2197*k2 + 7296/2197*k3)*h)
    k5 = func(t + h, u + (439/216*k1 - 8*k2 + 3680/513*k3 - 845/4104*k4)*h)
    k6 = func(t + 0.5*h, u + (-8/27*k1 + 2*k2 - 3544/2565*k3 + 1859/4104*k4 - 11/40*k5)*h)
    u_n = u + h * (25/216*k1 + 1408/2565*k3 + 2197/4104*k4 - 1/5*k5)
    err = h * (1/360*k1 - 128/4275*k3 - 2197/75240*k4 + 1/50*k5 + 2/55*k6)
    return u_n, err

def visualize(t, u_rk, u_imp, sol_sci):
    plt.figure(figsize=(10, 6))
    plt.plot(t, u_rk, 'ro', label='Explicit RK4', markersize=4, alpha=0.5, color='blue')
    plt.plot(t, u_imp, 'gx', label='Implicit RK4', color='purple')
    plt.plot(sol_sci.t, sol_sci.y[0], 'b', label='Embedded RKF 4(5)', linewidth=2, color='pink')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    h = 0.1
    #h = 1.1
    #h = 0.9
    print()
    steps = int((tk - t0) / h)
    t_vals = np.linspace(t0, tk, steps + 1)
    u_rk = [y0]
    u_imp_rk = [y0]
    u_rkf = [y0]
    err_rkf = [0.0]

    for i in range(steps):
        u_rk.append(runge_kutta4(t_vals[i], u_rk[-1], h))
        u_imp_rk.append(implicit_runge_kutta4(t_vals[i], u_imp_rk[-1], h))
        un, er = runge_kutta_fehlberg(t_vals[i], u_rk[-1], h)
        u_rkf.append(un)
        err_rkf.append(er)

    sol_sci = solve_ivp(func, [t0, tk], [y0], method='RK45', t_eval=t_vals)
    visualize(t_vals, u_rk, u_imp_rk, sol_sci)


