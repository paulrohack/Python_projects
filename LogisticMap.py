from matplotlib import pyplot as plt
import numpy as np
x = 0.2
i = 500
r = np.linspace(1, 4, 1000)
c = 0.1
cn = []
xn = []
for ln in range(len(r)):
    for n in range(i):
        x = r[ln]*x*(1-x)
        c += 0.1
        # print(x)
        cn.append(c)
        xn.append(x)
plt.figure("Logistic Map")
plt.title("x = xr(1 - xn)")
plt.plot(xn, '.', markersize=0.05)
plt.show()