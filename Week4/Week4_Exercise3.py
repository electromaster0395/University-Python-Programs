price = eval(input("Enter price: "))
print()

if(price > 300):
    print(price)
    print("30% discount applied")
    price *= 0.7
    print(price)

elif(price <= 300 and price > 200):
    print(price)
    print("20% discount applied")
    price *= 0.8
    print(price)

elif(price <= 200 and price >= 100):
    print(price)
    print("10% discount applied")
    price *= 0.9
    print(price)

else:
    print(price)
    print("5% discount applied")
    price *= 0.95
    print(price)
