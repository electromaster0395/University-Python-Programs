def factorial(number):
    result = 1
    for i in range(number):
        result *= i + 1
    return result

num = eval(input("Enter number: "))
print(factorial(num))
