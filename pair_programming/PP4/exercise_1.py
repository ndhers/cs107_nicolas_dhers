import numpy as np

def layer(shape, actv):
	def output(inputs, weights, bias):
		assert shape == weights.shape
		return actv(np.transpose(weights)@(inputs)+bias)
	return output


t = np.random.uniform(0.0, 1.0, 100).reshape(-1,1) # input to the network

shape1 = (100,10)
shape2 = (10,2)

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.uniform(size=(100,10))
w2 = np.random.uniform(size=(10,2))
b1 = np.random.uniform(size= (10,1))
b2 = np.random.uniform(size= (2,1))

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer	
# print(h1)
print(h2)