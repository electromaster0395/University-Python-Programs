import numpy
import random
from tabulate import tabulate

class Racer:
    #Racer meanSpeed is in ms^-1
    def __init__(self, pname, pmeanSpeed, pstandardDeviationOfSpeed):
        self.name = pname
        self.meanSpeed = pmeanSpeed
        self.standardDeviationOfSpeed = pstandardDeviationOfSpeed
        self.currentLapMeanSpeed = 0
        self.lapTimes = []
    
    def getName(self):
        return self.name
        
    def getMeanSpeed(self):
        return self.meanSpeed
        
    def getStandardDeviationOfSpeed(self):
        return self.standardDeviationOfSpeed

    def getCurrentLapMeanSpeed(self):
        return self.currentLapMeanSpeed

    def getLapTimesArray(self):
        return self.lapTimes

    def setName(x):
        self.name = x
        
    def setMeanSpeed(x):
        self.meanSpeed = x
        
    def setStandardDeviationOfSpeed(x):
        self.standardDeviationOfSpeed = x


    def updateLapSpeed(self):
        meanLapSpeed = numpy.random.normal(self.meanSpeed, self.standardDeviationOfSpeed, size = None)
        if(meanLapSpeed < 15):
            meanLapSpeed = 15 + random.uniform(0, 1)
            
        self.currentLapMeanSpeed = meanLapSpeed
        self.lapTimes.append(meanLapSpeed)
        print(self.lapTimes)

def makeRacersDoALap(array):
    for i in range(0, len(array)):
        array[i].updateLapSpeed()
    

def insertionSortArrayOfRacersByTime(racerArray):
    for number in range(1, len(racerArray)):
        while racerArray[number - 1].getCurrentLapMeanSpeed() > racerArray[number].getCurrentLapMeanSpeed() and number > 0:
            temp = racerArray[number-1]
            racerArray[number - 1] = racerArray[number]
            racerArray[number] = temp
            number -= 1
        return racerArray

def printRacerData(racerArray):
    racer2DArray = []
    headerArray = ["Name", "Average Track Speed", "Standard Deviation"]
    for i in range(1, NUMBER_OF_LAPS + 1):
        headerArray.append(str("Lap" + str(i)))
    print(headerArray)
        
    racer2DArray.append(headerArray)
    for i in range(0, len(racerArray)):
        tempArray = []
        tempArray.append(racerArray[i].getName())
        tempArray.append(round(racerArray[i].getMeanSpeed(), 2))
        tempArray.append(round(racerArray[i].getStandardDeviationOfSpeed(), 2))
        tempArray += racerArray[i].getLapTimesArray()
        racer2DArray.append(tempArray)
    print(tabulate(racer2DArray, headers='firstrow', tablefmt='fancy_grid', missingval='N/A'))
    print()
    return racer2DArray
            

TRACK_LENGHT = 10000 #Track lenght in meters
NUMBER_OF_LAPS = 3

while True:
    input("Race Simulator - Created by Omar")
    speedyBoi = Racer("Speedy Boi", 200, 1)
    slowBoi = Racer("Slow Boi", 150, 10)
    erraticBoi = Racer("Erratic Boi",150, 50)
    
    RacerArray = [speedyBoi, slowBoi, erraticBoi]

    makeRacersDoALap(RacerArray)

    RacerArray = insertionSortArrayOfRacersByTime(RacerArray)

    printRacerData(RacerArray)
