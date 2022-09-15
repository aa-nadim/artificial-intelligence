import math
x = math.factorial(4)
y = math.factorial(x)
print("Factorial of 4: ", x)
print("Factorial of(4!): ", y)
for i in range(5):
    y = float(math.sqrt(y))

print("The Float result: ", y)
