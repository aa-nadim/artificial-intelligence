#consider one hiddden layer
import  numpy as np
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]
                            ])
training_outputs = np.array([[0],
                            [1],
                            [1],
                            [0]])
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(x):
    return x*(1-x)
np.random.seed(1)
synaptic_weights = 2*np.random.random((3,1))-1 #3 inputs, 1 sample output, where the range from -1 to +1
print('\nRandom Initial Synaptic Weights: ')
print(synaptic_weights)
n=int(input("Enter number of Iteration: "))
for iteration in range(n):
    input_layer=training_inputs
    output=sigmoid(np.dot(input_layer,synaptic_weights))
    error=training_outputs-output
    adjustments = error*sigmoid_derivative(output)
    synaptic_weights=synaptic_weights+np.dot(input_layer.T, adjustments) #Updated synaptic weights after n epochs  training
print("\nThe number of Iteration:"+str(n))
print("\n Weights after training: ", synaptic_weights)
print("\nOutputs after training: ")
print(output)