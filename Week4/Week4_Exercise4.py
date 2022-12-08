def CelToFah(celsius):
    return (celsius * (9/5))+32

while True:
    Celsius = eval(input("Enter temperature in Celsius: "))
    print(CelToFah(Celsius))
