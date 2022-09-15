## NN architecture 3-4-1.
import numpy as np
def sigmoid(x):
    return 1/(1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1-x)
# Input = X
x = np.array([[0, 0, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])
# Target (Output) = t
t = np.array([[0],
            [1],
            [1],
            [0]])
np.random.seed(1)
# Initialize weights randomly with mean 0
w1 = 2 * np.random.random((3, 4)) - 1 # Since the number of hidden neuron is 4. And here, the number of input neuron
# is 3 and output neuron is 4
w2 = 2 * np.random.random((4, 1)) - 1 # Here the number of input neuron is four and output neuron is 1
print('Initial weights between Input Layer to Hidden Layer: ')
print(w1)
print('Initial weights between Hidden Layer to Output Layer: ')
print(w2)
print("Enter the number of epoch: ")
n=int(input())
for i in range(n):
    # Feed Forward through Input, Hidden and Output Layer
    Zi = sigmoid(np.dot(x, w1)) # z_in = sum(XiVi) = dot(X, Vi)
    # Output from Hidden Layer = Zi = f(z_in) = sigmoid_function(sum(XiVi))
    # Zi = sigmoid(np.dot(X,Vi)
    outputs = sigmoid(np.dot(Zi, w2))
    # y_in = sum(ZiWi) = dot(Zi, Wi)
    # Output from Output Layer = Yi = f(y_in) = sigmoid_function(sum(ZiWi))
    # Yi = sigmoid(np.dot(Zi,Wi)
    Yi_error = t - outputs # Error = Target - Network Output
    if (i % 10000) ==0:
        print("After",i,"Epoch Error:" +str(np.mean(np.abs(Yi_error))))
    # in what direction is the target value?
    # were we really sure? if so, don't change too much
    Yi_delta = Yi_error * sigmoid_derivative(outputs)
    # how much did each Zi value contribute to the Yi error according to the weights)?
    Zi_error = Yi_delta.dot(w2.T)
    # in what direction is the target Zi?
    # were we really sure? if so, don't change too much
    Zi_delta = Zi_error * sigmoid_derivative(Zi)
    w2 += Zi.T.dot(Yi_delta)
    w1 += x.T.dot(Zi_delta)
# Outputs
print('Outputs after training')
outputs = sigmoid(np.dot(Zi, w2))
print(outputs)
# Output for a new situation
Zi = sigmoid(np.dot(([1, 0, 0]), w1)) # Zi = nonlin(np.dot(X, Vi))
output = sigmoid(np.dot(Zi, w2)) # Yi = nonlin(np.dot(Zi, Wi))
print('Output for a new situation [1, 0, 0]')
print(output)
print("Final Weights: ",w1)