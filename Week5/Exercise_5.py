import random #import random library so I do not need to come up with a list of random values
randomlist = random.sample(range(10, 30), 10) #crease a random interger list with 10 intergers where each interger can be any interger between 10 and 30


#Define function that will return largest Nth number in list. Function takes in parameters of list and place
def findLargestN(numList, place):
    if(place > len(numList)): #Return nothing if place is larger than list lenght
        return None
    numList.sort()#Sort list from lowest to highes interger
    numList = numList[place-1:len(numList)] #Slice list so that the first item is the Nth largest item required from place parameter
    return numList[0] #Return first item of sorted list which is Nth largest interger


print(randomlist)
print(findLargestN(randomlist, 1))
