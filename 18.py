#************************Group_4**********************************#
#feed forward neural network

import numpy as np
x=np.array([[0,0,1],
            [1,1,1],
            [1,0,1],
            [0,1,1]])
t=np.array([[0],
            [1],
            [1],
            [0]])
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)
np.random.seed(1)
w=2*np.random.random((3,1))-1
print("\nRandom initial synaptic weights: ")
print(w)

n=int(input('Enter number of iteration: '))
for iteration in range(n):
    y=sigmoid(np.dot(x,w))
    error=t-y
    adjustments=error*sigmoid_derivative(y)
    w=w+np.dot(x.T,adjustments)

print("\nNumber of iteration:",n)
print("\nWeights after training: ")
print(w)
print("\noutputs after training: ")
print(y)