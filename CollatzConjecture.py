
def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    if n % 2 != 0:
        return int(3*n + 1)
    else:
        return 'Error'
 

n = int(input("Seed = "))
d = [n]
steps = 0
while n != 1:
    n = collatz(n)
    steps += 1
    d.append(n)
else:
    print(d)
    print(f"It Took {steps} steps")
    
