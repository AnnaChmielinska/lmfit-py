#!/usr/bin/env python

# <examples/doc_model_uncertainty.py>
import matplotlib.pyplot as plt
from numpy import exp, loadtxt, pi, sqrt

from lmfit import Model

data = loadtxt('model1d_gauss.dat')
x = data[:, 0]
y = data[:, 1]


def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x-cen)**2 / (2*wid**2))


gmodel = Model(gaussian)
result = gmodel.fit(y, x=x, amp=5, cen=5, wid=1)

print(result.fit_report())
dely = result.eval_uncertainty(sigma=3)

plt.plot(x, y, 'bo')
plt.plot(x, result.init_fit, 'k--')
plt.plot(x, result.best_fit, 'r-')
plt.fill_between(x, result.best_fit-dely, result.best_fit+dely, color="#ABABAB")
# plt.savefig('../doc/_images/model_fit4.png')
plt.show()
# <end examples/doc_model_uncertainty.py>