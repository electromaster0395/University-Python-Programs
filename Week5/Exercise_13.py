#n variable defines arrow size/height
n = 10

#Following for loop prints an ascending left hand side triangle with a height of 5
for i in range(n):
    for j in range(i):
        print("*", end = "")
    print()
#Following for loop prints descending left hand side triangle with a height of 4, ie: n-1 times
for i in range(n):
    for j in range(i, n):
        print("*", end = "")
    print()
