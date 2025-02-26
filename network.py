import random
import math

def tanh(x):
    return (2 / (1 + math.exp(-2 * x))) - 1

weights = [random.uniform(-0.5, 0.5) for _ in range(8)]

inputs = [0.05, 0.1]
bias_hidden = 0.5
bias_output = 0.7

hidden_outputs = [
    tanh((weights[0] * inputs[0]) + (weights[1] * inputs[1]) + bias_hidden),
    tanh((weights[2] * inputs[0]) + (weights[3] * inputs[1]) + bias_hidden)
]

output1 = tanh((weights[4] * hidden_outputs[0]) + (weights[5] * hidden_outputs[1]) + bias_output)
output2 = tanh((weights[6] * hidden_outputs[0]) + (weights[7] * hidden_outputs[1]) + bias_output)

print(f"Hidden Layer Outputs: h1 = {hidden_outputs[0]:.4f}, h2 = {hidden_outputs[1]:.4f}")
print(f"Output Layer Outputs: o1 = {output1:.4f}, o2 = {output2:.4f}")
