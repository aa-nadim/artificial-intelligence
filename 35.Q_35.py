# NN architecture 10-6-2.
import numpy as np

X = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
              [0, 9, 1, 8, 2, 7, 3, 6, 4, 5],
              [4, 5, 6, 3, 2, 7, 1, 8, 0, 9],
              [3, 8, 2, 7, 1, 6, 0, 5, 9, 4],
              [1, 6, 0, 7, 4, 8, 3, 9, 2, 5],
              [2, 1, 3, 0, 4, 9, 5, 8, 6, 7],
              [9, 4, 0, 5, 1, 6, 2, 7, 3, 8]])

t = np.array([[-1, -1],
              [1, 1],
              [-1, 1],
              [1, -1],
              [1, 1],
              [1, -1],
              [-1, 1],
              [-1, -1]])


def sigmoid(x):
    return (2 / (1 + np.exp(-x))) - 1


def sigmoid_derivative(x):
    return 0.5 * (x + 1) * (1 - x)


def training_with_bp(n):
    np.random.seed(1)
    # Initialize weights randomly with mean 0
    Vi = 2 * np.random.random((10, 6)) - 0.75
    Wi = 2 * np.random.random((6, 2)) - 0.75
    print('Initial weights between Input Layer to Hidden Layer: \n', Vi)
    print('Initial weights between Hidden Layer to Output Layer: \n', Wi)

    for epoch in range(n):
        # Feed Forward through Input, Hidden and Output Layer
        Zi = sigmoid(np.dot(X, Vi))  # Output from Hidden Layer = Zi = f(z_in) =sigmoid_function(sum(XiVi))
        Yi = sigmoid(np.dot(Zi, Wi))  # Output from Output Layer = Yi = f(y_in) = sigmoid_function(sum(ZiWi))
        Yi_error = t - Yi  # Error = Target - Network Output
    Yi_delta = Yi_error * sigmoid_derivative(Yi)
    # how much did each Zi value contribute to the Yi error according to the weights)?
    Zi_error = Yi_delta.dot(Wi.T)
    # in what direction is the target Zi?
    # were we really sure? if so, don't change too much
    Zi_delta = Zi_error * sigmoid_derivative(Zi)
    Wi += Zi.T.dot(Yi_delta)
    Vi += X.T.dot(Zi_delta)
    # Outputs
    print('Output after training')
    Yi = sigmoid(np.dot(Zi, Wi))
    outputs = Yi
    print(outputs)


print("\n\nFor Epoch 1000\n\n")
training_with_bp(1000)
print("\n\nFor Epoch 20,000\n\n")
training_with_bp(20000)
print("\n\nFor Epoch 60,000\n\n")
training_with_bp(60000)
