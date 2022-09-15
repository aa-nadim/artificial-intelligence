import numpy as np

x=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])

t=np.array([[0],
                           [0],
                           [1],
                           [1]])

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

np.random.seed(1)

vi=2*np.random.random((3,6))-1
wi=2*np.random.random((6,1))-1

print('\nRandom Initial weights between input and hidden layer: ')
print(vi)

print('\nRandom Initial weights between hidden and output layer: ')
print(wi)
n=int(input("enter the number of iteration "))

for j in range(n):
    #input_layer=training_inputs
    zi=sigmoid(np.dot(x,vi))
    yi=sigmoid(np.dot(zi,wi))
    yi_error=t-yi
    yi_delta=yi_error*sigmoid_derivative(yi)
    zi_error=yi_delta.dot(wi.T)
    zi_delta=zi_error*sigmoid_derivative(zi)
    wi+=zi.T.dot(yi_delta)
    vi+=x.T.dot(zi_delta)

print("\nfinal weights after training beetween input layer and hidden layer ")
print(vi)

yi=sigmoid(np.dot(zi,wi))
print("\nFinal Output:")
print(yi)