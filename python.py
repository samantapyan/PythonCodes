import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# yy'-2x(y')^2 = xyy'' y(1) = 1 y'(1) = -1

# u[0] = y
# u[1] = y'
# u[2] = y''
# u[0]u[1] -2x(u[1])^2 = xu[0]u[2]


def du_dx(u, x):
        return [u[0], u[1]]
u0 = [1,1]
xs = np.linspace(1,20,200)
us = odeint(du_dx, u0, xs)
ys = us[:,0]
plt.grid()
plt.xlabel('y')
plt.ylabel('x')
plt.title('ODE 2nd order IVP solved by SciPy with method=')
plt.plot(xs, ys, linewidth=1, label='numerical')
plt.show()



plt.legend()
plt.show()
