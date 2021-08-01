import numpy as np
import matplotlib.pylab as plt
import math as m


u = int(input("Velocity at which you throw the Ball: ")) 
g = 9.8
a = int(input("Angle or Theta with which you throw the Ball: ")) 
angle = [a * np.pi/180]

t = np.linspace(0, u/6, num= u*10)
# s = ti()
for i in angle:
    x_ = []
    y_ = []
    for k in t:
        x = ((u*k)*np.cos(i))
        y = ((u*k)*np.sin(i))-((0.5*g)*(k**2))
        if x > 0 and y > 0:
            x_.append(x)
            y_.append(y)
            
        
    plt.plot(x_, y_)
    # if a == 90:
    #     plt.xticks([-0.95, 0.0, 0.1])

R = round(((u**2)*np.sin(2*(angle[0])))/g, 2)
Tf = round(((u * np.sin(angle[0])))/ g, 2)
mH = round(((u * np.sin(angle[0]))**2)/(g*2), 2)

print("Range of the Projectile = ", R, "m")
print("Time of Flight of the Projectile = ", Tf, "s")
print("Maximum height of Projectile = ", mH, "m")

plt.plot([0], '.', markersize=20) #Initial Ball Position
plt.plot([R], [0], '.', markersize=20) #Final Ball Position
plt.plot([R/2], [mH], '.', markersize=20) #Maximum height of the Ball
# e = ti()

plt.show()
# print(e - s)
