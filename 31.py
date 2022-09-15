
import numpy as np
from numpy import *
input_layer=np.array([[1,-1],
             [-1,1],
             [1,1],
             [-1,-1]])
target=np.array([[1],
             [1],
             [-1],
             [-1]])

def sigmoid(X):
   return 1/(1+np.exp(-X))

def sigmoid_derivative(x):
    return x*(1-x)

print("Input = ",input_layer)
Vi=random.uniform(-0.5,0.5,(2,2))
Wi=random.uniform(-0.5,0.5,(2,1))
print('Initial Weights between input layer and hidden layer ',Vi)
print('Initial Weights between hidden layer and output layer ',Wi)

alpha=10e-6
n=int(input('Enter number of iteration : '))


for iteration in range(10000):
    hiddenoutput=sigmoid(np.dot(input_layer,Vi))
    output=sigmoid(np.dot(hiddenoutput,Wi))
    Yi_error=target-output
    # error1=np.dot(error2,w2.T)*hiddenoutput*(1-hiddenoutput)
    Yi_delta = Yi_error * sigmoid_derivative(output)
    Zi_error = np.dot(Yi_error, Wi.T)
    Zi_delta = Zi_error * sigmoid_derivative(hiddenoutput)
    Wi += np.dot(hiddenoutput.T, Yi_delta)
    Vi += np.dot(input_layer.T, Zi_delta)




output=sigmoid(np.dot(hiddenoutput,Wi))
print('Final Weights between input layer and hidden layer ',Vi)
print('Final Weights between hidden layer and output layer ',Wi)

print('Number of training epochs ',n)

print('Output')
print(output)
