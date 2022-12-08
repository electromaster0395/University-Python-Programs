import random

randnum = random.randint(0, 100)
num = 50

print("Number: ", num, ", Random Number: ", randnum)

if(num > randnum):
    print("Our number is bigger than the random")

elif(num < randnum):
    print("Our value is smaller than the random number")
else:
    print("Our number is equal to the random number")
