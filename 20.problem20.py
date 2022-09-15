import numpy as np

x=np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])

t=np.array([[0],
            [1],
            [1],
            [0]])

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

np.random.seed(1)

w= 2 * np.random.random((3, 1)) - 1

print('\nRandom Initial synaptic weights: ')
print(w)

n=int(input("enter the number of iteration "))

for iteration in range(n):
    outputs=sigmoid(np.dot(x, w))
    error= t - outputs
    adjustments=error*sigmoid_derivative(outputs)
    w= w + np.dot(x.T, adjustments)

print("\nthe number of iteration: " + str(n))
print("\n weights after training : ")
print(w)
print("\noutputs after training: ")
print(outputs)