## NN architecture 3-4-1.
import numpy as np
import numpy as np
import warnings

#suppress warnings
warnings.filterwarnings('ignore')
def sigmoid(x):
    return (1 - np.exp(-x))/(1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1-x)
# Input = X
x = np.array([[0,1,2,3,4,5,6,7,8,9],
              [9,8,7,6,5,4,3,2,1,0],
              [0,9,1,8,2,7,3,6,4,5],
              [4,5,6,3,2,7,1,8,0,9],
              [3,8,2,7,1,6,0,5,9,4],
              [1,6,0,7,4,8,3,9,2,5],
              [2,1,3,0,4,9,5,8,6,7],
              [9,4,0,5,1,6,2,7,3,8]])
# Target (Output) = t
t = np.array([[-1,-1],
            [1,1],
            [-1,1],
            [1,-1],
            [1,1],
            [1,-1],
            [-1,1],
            [-1,-1]])
np.random.seed(1)
# Initialize weights randomly with mean 0
w1 = 2 * np.random.random((10, 4)) - 1 # Since the number of hidden neuron is 4. And here, the number of input neuron
# is 3 and output neuron is 4
w2 = 2 * np.random.random((4, 2)) - 1 # Here the number of input neuron is four and output neuron is 1
print('Initial weights between Input Layer to Hidden Layer: ')
print(w1)
print('Initial weights between Hidden Layer to Output Layer: ')
print(w2)
#print("Enter the number of epoch: ")
#n=int(input())
for i in range(500):
    # Feed Forward through Input, Hidden and Output Layer
    Zi = sigmoid(np.dot(x, w1)) # z_in = sum(XiVi) = dot(X, Vi)
    # Output from Hidden Layer = Zi = f(z_in) = sigmoid_function(sum(XiVi))
    # Zi = sigmoid(np.dot(X,Vi)
    outputs = sigmoid(np.dot(Zi, w2))

    # y_in = sum(ZiWi) = dot(Zi, Wi)
    # Output from Output Layer = Yi = f(y_in) = sigmoid_function(sum(ZiWi))
    # Yi = sigmoid(np.dot(Zi,Wi)
    Yi_error = t - outputs # Error = Target - Network Output
    if (i % 100) ==0:
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
Zi = sigmoid(np.dot(([4,5,6,1,2,3,9,0,8,7]), w1)) # Zi = nonlin(np.dot(X, Vi))
output = sigmoid(np.dot(Zi, w2)) # Yi = nonlin(np.dot(Zi, Wi))
print('Output for a new situation [1, 0, 0]')
print(output)
print("Final Weights: ",w1)