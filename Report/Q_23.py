import numpy as np
def sigmoid(x):
    return 1/(1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1-x)
# Input = X
X = np.array([[0, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [0, 1, 1]])
# Target (Output) = t
t = np.array([[0],
        [1],
        [1],
        [0]])
np.random.seed(1)
# Initialize weights randomly with mean 0
Vi = 2*np.random.random((3, 4))-1 # Since the number of hidden neuron is 4. And here, the number of input neuron
# is 3 and output neuron is 4
Wi = 2*np.random.random((4, 1))-1 # Here the number of input neuron is four and output neuron is 1
print('Initial weights between Input Layer to Hidden Layer: ')
print(Vi)
print('Initial weights between Hidden Layer to Output Layer: ')
print(Wi)

for j in range(60000):
    # Feed Forward through Input, Hidden and Output Layer
    Zi = sigmoid(np.dot(X, Vi)) # z_in = sum(XiVi) = dot(X, Vi)
    # Output from Hidden Layer = Zi = f(z_in) = sigmoid_function(sum(XiVi))
    # Zi = sigmoid(np.dot(X,Vi)
    Yi = sigmoid(np.dot(Zi, Wi))
    # y_in = sum(ZiWi) = dot(Zi, Wi)
    # Output from Output Layer = Yi = f(y_in) = sigmoid_function(sum(ZiWi))
    # Yi = sigmoid(np.dot(Zi,Wi)
    Yi_error = t - Yi # Error = Target - Network Output
    if (j% 10000) ==0:
        #print("Error: ", Yi_error)
        print("Error:",np.mean(np.abs(Yi_error)))
# in what direction is the target value?
# were we really sure? if so, don't change too much
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
# Output for a new situation
Zi = sigmoid(np.dot(([1, 0, 0]), Vi))  # Zi = nonlin(np.dot(X, Vi))
Yi = sigmoid(np.dot(Zi, Wi))  # Yi = nonlin(np.dot(Zi, Wi))
output = Yi
print('Output for a new situation [1, 0, 0]')
print(output)