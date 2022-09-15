import numpy as np

x = np.array([[0, 1, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])
t = np.array([[0],
              [1],
              [1],
              [0]])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def training_with_bp(n):
    np.random.seed(1)
    w = 2 * np.random.random((3, 1)) - 1
    # print('Random initial synaptic Weights\n',w)

    for epoch in range(n):
        output = sigmoid(np.dot(x, w))
        error = t - output
        adjustment = error * sigmoid_derivative(output)
        w = w + np.dot(x.T, adjustment)

    print('Weights after training\n',w)
    print('Outputs after training',output)
    print(error)


print("Error when epooch is 1000")
training_with_bp(1000)
print("Error when epooch is 5000")
training_with_bp(5000)
print("Error when epooch is 10000")
training_with_bp(10000)
print("Error when epooch is 50000")
training_with_bp(50000)
print("Error when epooch is 100000")
training_with_bp(100000)

