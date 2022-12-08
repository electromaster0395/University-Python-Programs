My_list = [30, 21, 16, 66, 78, 109, 1, 4, 52] #Define list containing numbers


#This function returns max number in given list parameter
def maxNum(nList):

    #Return "None" if the passes nList has no items or has lenght of 0
    if(len(nList) == 0):
        return None

    #Begin assuming first item in list is the largest number and assign it to a variable of appropiate name
    largestNum = nList[0]

    #Iterage through every other list item and swap "largestNum" with "currentNumber" if currentNumber > largestNum 
    for i in range(1, len(nList)):
        currentNum = nList[i]
        if(largestNum < currentNum):
            largestNum = currentNum

    #return "largestNum" variable
    return largestNum


#Print largest number in "My_list" number list
print(maxNum(My_list))
            
