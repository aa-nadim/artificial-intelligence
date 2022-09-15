############################################DIABETES DATABASE###########################################################################
from tabulate import tabulate

#CREATE TABLE
patients=[['Id', 'Name', 'Age', 'Weight(kg)', 'Height(m)', 'Blood Pressure(mmHg)', 'Working status', 'Marital status', 'Father\'s diabetes status', 'Mother\'s diabetes status', 'Any Heart disease status', 'Any liver disease status'],
                   ['1', 'Mirza', '40', '67', '1.75', '140/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['2', 'Rahat', '50', '79', '1.63', '130/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['3', 'Khan', '30', '85', '1.8', '120/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['4', 'Raquib', '46', '72', '1.7', '120/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['5', 'Asadullah', '58', '65', '1.65', '130/80', 'Employed', 'Married ', 'Positive', 'Negative', 'Negative', 'Negative'],
                   ['6', 'Galib', '32', '101', '1.62', '120/80', 'Employed', 'Married ', 'Positive', 'Negative', 'Negative', 'Negative'],
                   ['7', 'Shamshad', '55', '76', '1.73', '130/80', 'Employed', 'Married ', 'Positive', 'Negative', 'Negative', 'Negative'],
                   ['8', 'Rasib', '43', '92', '1.59', '120/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['9', 'Faridul', '59', '50', '1.77', '140/70', 'Unemployed', 'Married ', 'Negative', 'Positive', 'Negative', 'Negative'],
                   ['10', 'Alam', '62', '55', '1.735', '130/80', 'Unemployed', 'Married ', 'Negative', 'Positive', 'Negative', 'Negative'],
                   ['11', 'Setara', '39', '59', '1.68', '140/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['12', 'Khanam', '68', '51', '1.72', '140/90', 'Unemployed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['13', 'Akib', '51', '67', '1.79', '140/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['14', 'Sifat', '35', '79', '1.9', '120/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative'],
                   ['15', 'Imdad', '60', '61', '1.69', '140/80', 'Employed', 'Married ', 'Negative', 'Negative', 'Negative', 'Negative']]
#SHOW TABLE
print(tabulate(patients, headers="firstrow", tablefmt="fancy_grid"))

#################################################Backpropagation Neural Network###########################################################
#feed forward neural network

import numpy as np
x=np.array([[0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,1,1],
            [1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,1]])
t=np.array([[0],
            [0],
            [1],
            [1]])
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)
np.random.seed(1)
w=2*np.random.random((8,1))-1
w=w*0.8
w2=2*np.random.random((8,1))-1
w2=w2*0.8
print("\nRandom initial weights for output y: ")
print(w)
print("\nRandom initial weights for output y2: ")
print(w2)

n=int(input('enter number of iteration: '))#5000, 50000#
for iteration in range(n):
    y=sigmoid(np.dot(x,w))
    y2=sigmoid(np.dot(x,w2))
    error=t-y
    error2=t-y2
    adjustments=error*sigmoid_derivative(y)
    adjustments2=error2*sigmoid_derivative(y2)
    w=w+np.dot(x.T,adjustments)
    w2=w2+np.dot(x.T,adjustments2)

print("\nNumber of training epochs:",n)
print("\nFinal Weights for y after training: ")
print(w)
print("\nFinal Weights for y2 after training: ")
print(w2)
print("\nNetwork response of y after training: ")
print(y)
print("\nNetwork response of y2 after training: ")
print(y2)