#Function takes in an interger number as parameter which represents amount of numbers printed from fibonacci sequence
def fib(number):
    #First number and second number of sequence are 0 and 1 respectively which are printed out
    firstNum = 0
    secondNum = 1
    print(firstNum, secondNum, sep = "\n")
    #Print sum of first and second number, then set first number to be equal to second number and second number to be equal to new number
    #For loop will print from 3rd to "number" digits of fibonnacci sequence by repeating number-3 iterations of printing out a new fibonacci character
    for i in range(secondNum, number-1):
        newNum = firstNum + secondNum
        print(newNum)
        firstNum = secondNum
        secondNum = newNum

#Print first 100 characters in Fibonacci sequence
fib(100)
        
        
