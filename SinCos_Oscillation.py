import matplotlib.pyplot as plt
from  numpy import cos, sin, arange, pi

x_val = arange(0.0, 1.0, 0.001)

normal = []
for n in range(len(x_val)):
    normal.append(0)

r = 2 * pi

def sin_f():
    return sin(x_val * r) 
def cos_f():
    return cos(x_val * r) 

# print(s)
plt.plot(x_val, cos_f())
plt.plot(x_val, sin_f())
plt.plot(x_val, normal)



plt.grid()
plt.show()