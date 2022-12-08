def cube(number):
    return number*number*number

def divisibleBy3(number):
    return number%3 == 0

while True:
    inputNum = eval(input("Enter number: "))
    if(divisibleBy3(inputNum)):
        print("Number is divisible by 3\nCubed number is: ", cube(inputNum))

    else:
        print("Number NOT divisible by 3")
