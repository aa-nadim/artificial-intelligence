import numpy as np
def sigmoid(x):
    return 1/(1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1-x)
X = np.array([[0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]])
t = np.array([[0],
        [0],
        [1],
        [1]])
np.random.seed(1)
Vi = 2*np.random.random((3, 6))-1
Wi = 2*np.random.random((6, 1))-1
for j in range(60000):
    Zi = sigmoid(np.dot(X, Vi))
    Yi = sigmoid(np.dot(Zi, Wi))
    Yi_error = t - Yi
    if (j% 5000) ==0:
        print("Error After",j,"Epoch:",np.mean(np.abs(Yi_error)))
    Yi_delta = Yi_error * sigmoid_derivative(Yi)
    Zi_error = Yi_delta.dot(Wi.T)
    Zi_delta = Zi_error * sigmoid_derivative(Zi)
    Wi += Zi.T.dot(Yi_delta)
    Vi += X.T.dot(Zi_delta)
print("\nFinal Weights between input layer to hidden layer after 60000 epochs:")
print(Vi)
print("\nFinal weights between hidden layer to output layer after 60000 epochs:")
print(Wi)