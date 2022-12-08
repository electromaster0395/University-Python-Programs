#Function takes in list of numbers as parameter and sums every possible combination of a number pair within passed list
#If any combination sum is 0, then the function returns true
def check_sum(List):
    for i in range(0, len(List)):
        for j in range(0, len(List)):
            currentSum = List[i]-List[j]
            if(currentSum == 0):
                return True

    return False

#Define two lists to test each possible outcome, one which should return true and another that whould return false
trueList = [10,15,-6, 2, 6, 7, 21]
falseList = [10,15,-6, 2, 5, 7, 21]

#Print list results
print(check_sum(trueList))
print(check_sum(falseList))
