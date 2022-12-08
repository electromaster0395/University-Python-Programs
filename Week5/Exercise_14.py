#Define string examples of each case where a string can have balanced brackets, unbalance brackets or be empty
brackets_balanced = "[[[[[[[]]]]]]]"
empty = ""
brackets_unbalanced = "[[[[[[]]]]]"


#Function returns True if string is empty or balanced. Returns false otherwise
def balance(String):

    #Return true if string is empty ie: has no characters
    if(len(String) == 0):
        return True

    #Define variables to count left and right brackets
    rightBrackets = 0
    leftBrackets = 0

    #Iterate through each character in string in order to count number of left and right brackets
    for i in range(0, len(String)):
        currentChar = String[i]
        if(currentChar == "["):
            rightBrackets += 1
        elif(currentChar == "]"):
            leftBrackets += 1

    #If right brackets amount is not equal to left brackets amount, then return False, return True otherwise
    if(rightBrackets != leftBrackets):
        return False

    else:
        return True
    
#Print return result of each string case
print(balance(brackets_balanced))
print(balance(brackets_unbalanced))
print(balance(empty))
