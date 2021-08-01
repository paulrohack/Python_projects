
from matplotlib import pyplot as plt
import math

index = [0]
pi = math.pi
sequence = [0]
plt.figure(f"Recaman's Sequence Visualization")

def recaman(n):
    count = 0
    a = [0] * n
    a[0] = 0
    print(a[0], end="\n")
    for i in range(1, n):
        c = a[i-1] - i

        for j in range(0, i):
            if ((a[j] == c) or c < 0):
                c = a[i-1] + i
                break
        a[i] = c
        count += 1
        index.append(count)
        print(a[i], end="\n")
        sequence.append(a[i])
    ask = input("Do you want to visualize it [s/n]: ")
    if ask.upper() == 'S':
        plt.plot(index, sequence)
        plt.show()
    else:
        pass


n = int(input("How Long should the sequence go (n = ): "))
plt.title(f"n = {n}")
recaman(n)


