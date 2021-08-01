from math import pow, pi
from matplotlib import pyplot as plt

l = []
n = 0
nl = []
p = []

print(f"Number of Digits of  π ≈ {pi}  also effects the accuracy of the value")
print("More the Digits == More Time it takes")

digits = int(input("Digits in Pi : "))
d = int(pow(10, digits))

print("Computing.....")
for  i in range(1, d, 2):
    l.append(1/i)
for e in range(d//2):
    if e % 2 != 0:
        l[e] *= -1
for c in range(len(l)):
    n += l[c]
for m in range((len(l))):
    nl.append(m)
    p.append(0)
s = 4 * n

print(f"π ≈ {round(s, digits)}")

# plt.figure(f"Leibniz formula for π")
# plt.title(f"π Digits = {digits}")
# plt.plot(nl, p, 'red', linewidth=1.5)
# plt.plot(nl, l, 'cyan', linewidth=0.25)
# plt.show()

