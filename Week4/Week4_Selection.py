grade = eval(input("Enter grade:"))

result = ""

if(grade > 90):
    result = "A"

elif(grade > 80):
    result = "B"

elif(grade > 70):
    result = "C"

elif(grade >= 60):
    result = "D"
    
else:
    result = "F"

if(result == "F"):
    difference = 60-grade
    print("You failed, you got an ", result, ". You need ", difference, " more mark(s) to pass")
else:
    print("You passed, you got an ", result,". You are cool")
