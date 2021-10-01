# Team members:
# Angel Hsu
# Mingcheng Liu
# Nicolas Dhers


import math
import numpy as np

class Layer:
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weights = np.random.uniform(shape[0], shape[1])
        self.bias = np.random.uniform(1, shape[1])

    def forward(self, inputs):
        output = self.actv(np.dot(inputs, self.weights) + self.bias)
        return output

    def __str__(self):
        return f"Our weights are {self.weights}"


    def __repr__(self):
        return f"Our Layer's shape is {self.shape}"

    def __len__(self):
        return self.shape[0]

inputs = np.random.uniform(size = (1,2))
shape1 = [2,3]
shape2 = [3,1]
actv = np.tanh

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)

# Demo

# Check if __str__ working
print(layer1)

# Check if __repr__ working
print(repr(layer1))

# Check if __len__ working
print(len(layer1)) 









