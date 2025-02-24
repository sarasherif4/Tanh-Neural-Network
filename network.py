import random
import math

w1, w2, w3, w4, w5, w6, w7, w8 = [random.uniform(-0.5, 0.5) for _ in range(8)]

i1 = 0.05
i2 = 0.1

b1 = 0.5
b2 = 0.7


def tanh(x):
    return (2 / (1 + math.exp(-2 * x))) - 1


net_h1 = (w1 * i1) + (w2 * i2) + b1
net_h2 = (w3 * i1) + (w4 * i2) + b1

out_h1 = tanh(net_h1)
out_h2 = tanh(net_h2)

net_o1 = (w5 * out_h1) + (w6 * out_h2) + b2
net_o2 = (w7 * out_h1) + (w8 * out_h2) + b2

out_o1 = tanh(net_o1)
out_o2 = tanh(net_o2)

print(f"out_h1 = {out_h1:.4f}")
print(f"out_h2 = {out_h2:.4f}")
print(f"out_o1 = {out_o1:.4f}")
print(f"out_o2 = {out_o2:.4f}")
