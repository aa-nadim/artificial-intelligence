import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

x = np.array([[0, 0, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])

t = np.array([[0], [1], [1], [0]])

np.random.seed(1)

vi = 2 * np.random.random((3, 8)) - 1

wi = 2 * np.random.random((8, 1)) - 1
print('initial weights between input layer to hidden layer:')
print(vi)
print('initial weights between hidden layer to output layer:')
print(wi)

for j in range(60000):
    zi = sigmoid(np.dot(x, vi))

    yi = sigmoid(np.dot(zi, wi))

    yi_error = t - yi

    yi_delta = yi_error * sigmoid_derivative(yi)

    zi_error = yi_delta.dot(wi.T)
    #print("ERROR EFFECT")

    zi_delta = zi_error * sigmoid_derivative(zi)

    wi += zi.T.dot(yi_delta)
    vi += x.T.dot(zi_delta)

"""print("ERROR EFFECT")
print(yi_error)
print(zi_error)"""

print('Final weights after training between input and hidden layer: ')
print(vi)
print('Final weights after training between hidden and output layer: ')
print(wi)
yi = sigmoid(np.dot(zi, wi))
#print(yi)