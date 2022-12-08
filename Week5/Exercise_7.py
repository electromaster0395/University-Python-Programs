import random

#Make a random list with 10 numbers within whereby each can be anywhere between 0 and 100
randomList = random.sample(range(0, 100), 10)

#Declare "high" and "low" lists
highList = []
lowList = []

#Loop iterates through eack item of randomList. If current item is divisible by 4 or higher than 50, it is appended to highlist, otherwise it is appended to lowList
for i in range(0, len(randomList)):
    currentNum = randomList[i]
    if(currentNum%4 == 0 or currentNum > 50):
        highList.append(currentNum)
    else:
        lowList.append(currentNum)

#Create a list called H_L which contains only two items: number of items in highList and lowList respectively
H_L = [len(highList), len(lowList)]

#Print all the declared list within the script
print(randomList, "\n")
print(highList, "\n")
print(lowList, "\n")
print(H_L)
