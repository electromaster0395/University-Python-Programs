#Declare starting number "num" as "10"
num = 10

#Print each num decrement but skip 6 and stop once decrement is 1
while num != 1:
    #Decrement number by 1
    num -= 1
    #Skip loop iteration if current decrement is 6
    if(num == 6):
        pass
    print(num + 1)
    
