#consider one hiddden layer
#3-4-1
import  numpy as np
x = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]
                            ])
#training_outputs\
    y= np.array([[0],
                            [1],
                            [1],
                            [0]])
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(x):
    return x*(1-x)
np.random.seed(1)

w1 = 2*np.random.random((3, 4))-1 #3x4 Weight matrix from input to hidden layer
w2 = 2*np.random.random((4, 1))-1 #4x1 Weight matrix from hidden to output layer
print('\nRandom Initial Weights between input layer and hidden layer: ')
print(w1)
print('\nRandom Initial Weights between hidden layer and output layer: ')
print(w2)
n=int(input("Enter number of Iteration: "))
for iteration in range(n):
    zi=sigmoid(np.dot(x,w1)) #Output of hidden layer
    yi = sigmoid(np.dot(zi,w2)) #Output of output layer
    yi_error=t-yi
    if (j%10000==0):

    yi_delta= yi_error*sigmoid_derivative(yi)
    zi_error=yi_delta.dot(Wi.T)
    zi_delta=zi_error*sigmoid_derivative(zi)

    w1+=zi.T(yi_delta)
    v1+=training_inputs.T
    input_layer=training_inputs
    output=sigmoid(np.dot(input_layer,synaptic_weights))
    error=training_outputs-output
    adjustments = error*sigmoid_derivative(output)
    synaptic_weights=synaptic_weights+np.dot(input_layer.T, adjustments) #Updated synaptic weights after n epochs  training
print("\nThe number of Iteration:"+str(n))
print("\n Weights after training: ", synaptic_weights)
print("\nOutputs after training: ")
print(output)