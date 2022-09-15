import numpy as np

input=np.array([[1,1,1],
       [1,0,1],
       [0,1,1],
       [0,0,1]])
target=np.array([[1],
        [-1],
        [-1],
        [-1]])

def sigmoid(X):
    return 1/(1+np.exp(-X))

def sigmoid_derivative(X):
    return X*(1-X)

np.random.seed(1)
#w=np.random.uniform(-0.5,0.5,(3,1))
w=2*np.random.random((3,1))-1
alpha=10e-6
print('Initial weights = ' ,w)
for i in range(20000):
    output=sigmoid(np.dot(input,w))
    error=target-output
    adjustment=error*sigmoid_derivative(output)
    w=w+alpha*np.dot(input.T,adjustment)

output=sigmoid(np.dot(input,w))
print('New weight = ',w)
print('Output = ',output)

