import matplotlib.pyplot as plt

def collatz(n):
    if n%2 == 0:
        return n/2
    return (3*n)+1

def generate(n):
    num = 0
    nums = [n]
    while n!=1:
        n = collatz(n)
        if n == 1:
            nums.append(n)
            num+=1
            print(f'It took {num} steps to get to 1')
            break
        else:
            nums.append(n)
            num+=1
    return nums
for i in range(1,3000):
    plt.plot(generate(i))
plt.show()