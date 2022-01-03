import argparse
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
            print(f'It took {num} step(s) to get to 1')
            break
        else:
            nums.append(n)
            num+=1
    return nums

parser = argparse.ArgumentParser()
parser.add_argument('--num',default=2)
parser.add_argument('--log_scale',default=False)
args = parser.parse_args()
if bool(args.log_scale):plt.yscale('log')
plt.plot(generate(int(args.num)))
plt.show()

# for i in range(1,3000):
#     plt.plot(generate(i))
# plt.show()