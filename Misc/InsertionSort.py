arrayToBeSorted = [2, 8, 5, 9, 1, 90, 30, 20, 10, 59, 21, 10, 30, 99, 32]

print(arrayToBeSorted)

def InsertionSort(array):
    for number in range(1, len(array)):
        while array[number - 1] > array[number] and number > 0:
            temp = array[number - 1]
            array[number - 1] = array[number]
            array[number] = temp
            number -= 1
        print(array)
    return array

print(InsertionSort(arrayToBeSorted))
