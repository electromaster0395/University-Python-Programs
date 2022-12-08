import math

#Declare original tuple "tup" and newTup as a list since tuples are immutable and cannot be changed during runtime
tup = (1, 3, 5, 7)
newTup = []

#Iterate through original tuple and append each original tuple item to new tuple but raised to the power of 2
for i in range(0, len(tup)):
    newTup.append(math.pow(tup[i], 2))

#Convert new tuple list to a tuple
newTup = tuple(newTup)

#Print contents of both tuples
print("Original tuple: ", tup, "\n New tuple: ", newTup)
print(type(newTup))
