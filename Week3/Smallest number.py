import random

randomNumberList = []

nIterations = int(input("Enter random number list size: "))

for i in range(0, nIterations):
    randomNum = random.randint(0, 1000)
    randomNumberList.append(randomNum)


smallest = randomNumberList[0]

for i in randomNumberList:
    if(smallest > i):
        smallest = i

print(smallest)

print(randomNumberList)
