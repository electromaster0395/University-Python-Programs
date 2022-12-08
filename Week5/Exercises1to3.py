L1 = [] #Define an empty list/array called L1
L2 = [] #Define an empty list/array called L2
L3 = [] #Define an empty list/array called L3

#This loop adds intergers 1-30 to L1
for i in range(1, 31): #Iterate 30 times in order to add desired amount of intergers
    L1.append(i) #Append current interger to list/array

#This loop adds only even numbers of L1 to L2
for i in range(0, len(L1)):
    currentNumber = L1[i]
    if(currentNumber%2 == 0):
        L2.append(currentNumber)

#This loop adds only the first 5 elements of L2 to L3
for i in range(0, 5):
    L3.append(L2[i])

print("L1: ", L1, "\n", "L2: ", L2, "\n", "L3: ", L3) #Print resulting L1 and L2s
