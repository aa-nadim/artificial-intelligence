import numpy as np
import warnings
warnings.filterwarnings('ignore')
def sigmoid(x):
    return (2/(1+np.exp(-x)))-1
def sigmoid_derivative(x):
    return 0.5*(1+x)*(1-x)
x=np.array([[0,1,2,3,4,5,6,7,8,9],
            [9,8,7,6,5,4,3,2,1,0],
            [0,9,1,8,2,7,3,6,4,5],
            [4,5,6,3,2,7,1,8,0,9],
            [3,8,2,7,1,6,0,5,9,4],
            [1,6,0,7,4,8,3,9,2,5],
            [2,1,3,0,4,9,5,8,6,7],
            [9,4,0,5,1,6,2,7,3,8]])
t=np.array([[-1,-1],
            [1,1],
            [-1,1],
            [1,-1],
            [1,1],
            [1,-1],
            [-1,1],
            [-1,-1]])
np.random.seed(1)
w = 2*np.random.random((10,2))-1
print("Initial weight")
print(w)
n=int(input("Enter the number of Iteration: "))
for iteration in range(n):
    y=sigmoid(np.dot(x,w))
    error=t-y
    adjustment=error*sigmoid_derivative(y)
    w=w+np.dot(x.T,adjustment)
print("Final weight after training:")
print(w)
print("Network response after training:")
print(y)