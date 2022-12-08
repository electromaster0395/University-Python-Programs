#Declare original "L" array as a tuple and new tuple "new_L" as a list since it needs to be mutated
L = [(2,4,6), (1,3,5), (10,20,30)]
new_L = []

#Iterate through every row and then iterate through every row item in order to iterate through every 2D tuple item
for i in range(0, len(L)):
    #Declare row empty temporary to be added to new tuple
    tempRow = []
    for j in range(0, len(L[i])):
        #Append product of row number and current attribute/cell to temporary row
        tempRow.append(L[i][j] * i)

    #Append temporary row to new tuple
    new_L.append(tempRow)

new_L = tuple(new_L)
print("L: ", L, "\nNew L: ", new_L)
