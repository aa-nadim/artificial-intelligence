import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

x = np.array([[1, -1],
              [-1, 1],
              [1, 1],
              [-1, -1]])

t = np.array([[1], [1], [-1], [-1]])

np.random.seed(1)

vi = 2 * np.random.random((2, 6)) - 1
vi*=0.5
wi = 2 * np.random.random((6, 1)) - 1
wi*=0.5
#weights are randomly distributed on (-0.5, 0.5)
print('initial weights between input layer to hidden layer:')
print(vi)
print('initial weights between hidden layer to output layer:')
print(wi)

n=int(input("Enter number of epoches: "))#1000, 10000, 25000
for j in range(n):
    zi = sigmoid(np.dot(x, vi))

    yi = sigmoid(np.dot(zi, wi))

    yi_error = t - yi

    yi_delta = yi_error * sigmoid_derivative(yi)

    zi_error = yi_delta.dot(wi.T)

    zi_delta = zi_error * sigmoid_derivative(zi)

    wi += zi.T.dot(yi_delta)
    vi += x.T.dot(zi_delta)

print('Final weights after training between input and hidden layer: ')
print(vi)
print('Final weights after training between hidden and output layer: ')
print(wi)
yi = sigmoid(np.dot(zi, wi))
print("Output after training: ")
print(yi)